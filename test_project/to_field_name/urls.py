from django.urls import path

from . import views

urlpatterns = [
    path("case-autocomplete/", views.CaseAutocomplete.as_view(), name="case_autocomplete"),
    path("cases-basic/", views.CaseFormBasicView.as_view(), name="case_form"),
    path("cases-ac/", views.CaseFormAutocompleteView.as_view(), name="case_form"),
]
