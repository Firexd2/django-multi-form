from django.http import HttpResponseRedirect
from django.views.generic.base import ContextMixin


class MultiFormMixin(ContextMixin):

    form_classes = {}
    form_instances = {}
    form_initials = {}
    form_success_urls = {}

    form_name = None

    def redirect_to_success_url(self):
        return HttpResponseRedirect(self.get_success_url())

    def get_initial(self, form_name):

        attr_name = 'get_initial_form_' + form_name
        default = self.form_initials.get(form_name)

        initial = getattr(self, attr_name, default)

        if callable(initial):
            return initial()
        else:
            return initial

    def get_instance(self, form_name):

        attr_name = 'get_instance_form_' + form_name
        default = self.form_instances.get(form_name)

        instance = getattr(self, attr_name, default)

        if callable(instance):
            return instance()
        else:
            return instance

    def get_success_url(self):

        attr_name = 'get_success_url_form_' + self.form_name
        default = self.form_success_urls.get(self.form_name)

        success_url = getattr(self, attr_name, default)

        if callable(success_url):
            return success_url()
        else:
            return success_url or self.request.get_full_path()

    def general_valid_form(self, form):
        form.save()
        return self.redirect_to_success_url()

    def general_invalid_form(self, form):
        data = self.get_context_data(**{'form_' + self.form_name: form})
        return self.render_to_response(data)

    def post(self, *args, **kwargs):

        # to get all the names in POST and FILES
        data_names = set()
        data_names.update(set(self.request.POST.keys()))
        data_names.update(set(self.request.FILES.keys()))

        # for a successful comparison, you must delete csrfmiddlewaretoken
        # because otherwise it will not be possible to determine the form
        data_names.remove('csrfmiddlewaretoken')

        # looking for a form
        for form_name in self.form_classes:

            # to get the form by name
            form = self.form_classes[form_name]
            # to get all the names of the form
            field_form_names = set(form.base_fields.keys())

            # compare the names
            if field_form_names == data_names:

                # fill out the form with data
                form = form(self.request.POST,
                            self.request.FILES,
                            instance=self.get_instance(form_name))

                # for convenience, remember the name of the form
                self.form_name = form_name

                # normal form validation
                if form.is_valid():
                    handler = getattr(self, 'form_valid_' + form_name, self.general_valid_form)
                else:
                    handler = getattr(self, 'form_invalid_' + form_name, self.general_invalid_form)
                return handler(form)

    def get_form(self, form_name):

        form = self.form_classes[form_name]

        return form(initial=self.get_initial(form_name),
                    instance=self.get_instance(form_name))

    def get_context_data(self, *args, **kwargs):
        context = super(MultiFormMixin, self).get_context_data(**kwargs)

        # output all forms to the template
        for form_name in self.form_classes:
            if 'form_' + form_name not in kwargs:
                context['form_' + form_name] = self.get_form(form_name)
        return context
