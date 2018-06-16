This library allows your to use unlimited number of forms in your views.

Add forms to the dict form_classes, where the key is the form name,
and the value is the form class.

By default, in the case of validation, there is form.save(),
else there is the error output to the template.

To change this behavior,
in the processing form.valid use form_valid_my_form(self, form),
and form_invalid_my_form(self, form) for form.invalid.

If you want to fill out the form, use the dict form_initials, where the key is the form name,
and the value is the dict, in which the key is field name, and the value is the field value.
Ex.: {'my_form': {'first_name': 'Denis', 'city': 'Moscow'}}

Or define a special method get_initials_form_my_form(self), and return the data dictionary.

If you need to update the object, use dict form_instances, where the key in the form name,
and the value is the object.

You can also define a special method get_instances_form_my_form(self).

By default, if form proccesing is successful it will be redirected to the same page.

You can change this behavior, by writting a new key and value in the dict form_success_urls.

You can also use a special method get_success_url_form_my_form(self) to procces the redirect site.