from django.views.generic.base import TemplateView

from multi_form.mixin import MultiFormMixin


class MultiFormView(MultiFormMixin, TemplateView):
    """
    generic template multiform view
    """
