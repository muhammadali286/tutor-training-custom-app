"""
URLs for training_custom_django_app.
"""
from django.urls import re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    re_path(r'/abc', TemplateView.as_view(template_name="training_custom_django_app/base.html")),
]
