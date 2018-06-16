# Django Multi Form

Django class based views for using more than one Form in a single view.

## Install
```bash
$ pip install django-multi-form
```

For usage django-multi-form, you can usage mixin to create the required class, e.x.:

```python
from django.views.generic.base import TemplateView

from multi_form.mixin import MultiFormMixin


class YourView(MultiFormMixin, TemplateView):

...

```

or use ready-make classes:

```python
from multi_form.generic import MultiFormView, DetailMultiFormView, ListMultiFormView
```

## Usage

### Add/output

Add forms to the dict form_classes, where the key is the form name, and the value is the form class:

```python
form_classes = {'my_form': FirstFormClass,
                'my_form_second': SecondFormClass}
```

In template for output forms usage:

```bash
{{ form_my_form }}

{{ form_my_form_second }}

```

### Validation

By default, in the case of validation, there is the method:

 ```python
def general_valid_form(self, form):
    form.save()
    return self.redirect_to_success_url()
 ```

else there is the error output to the template, i.y.:

```python
def general_invalid_form(self, form):
    data = self.get_context_data(**{'form_' + self.form_name: form})
    return self.render_to_response(data)
```
**To change this behavior**, in the processing form.valid use form_valid_my_form(self, form):

```python
def form_valid_my_form(self, form):
    pass
```

and form_invalid_my_form(self, form) for form.invalid:

```python
def form_invalid_my_form(self, form):
    pass
```

### Fill out the form

If you want to fill out the form, use the dict ```form_initials```, where the key is the form name,
and the value is the dict, in which the key is field name, and the value is the field value.

```python
form_initials = {'my_form': {'first_name': 'Denis', 'city': 'Moscow'},
                 'my_form_second': {'phone': '+799999999'}}
```

Or define a special method ```get_initials_form_my_form(self)```, and return the data dictionary.

### Update the object

If you need to update the object, use dict ```form_instances```, where the key in the form name,
and the value is the object.

You can also define a special method ```get_instances_form_my_form(self)```.

### Redirect to success url

By default, if form proccesing is successful it will be redirected to the same page.
You can change this behavior, by writting a new key and value in the dict ```form_success_urls```.
You can also use a special method ```get_success_url_form_my_form(self)``` to procces the redirect site.
