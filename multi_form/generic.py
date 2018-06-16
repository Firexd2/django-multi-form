from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from multi_form.mixin import MultiFormMixin


class MultiFormView(MultiFormMixin, TemplateView):
    """
    generic MultiFormMixin with TemplateView
    """


class DetailMultiFormView(MultiFormMixin, DetailView):
    """
    generic MultiFormMixin with DetailView
    """


class ListMultiFormView(MultiFormMixin, ListView):
    """
    generic MultiFormMixin with ListView
    """
