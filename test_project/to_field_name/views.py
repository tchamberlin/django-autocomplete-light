from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from dal import autocomplete

from .models import Case
from .forms import CaseFormBasic, CaseFormAutocomplete

class CaseAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        cases = Case.objects.order_by("case_num")
        if self.q:
            cases = cases.filter(case_num__istartswith=self.q).order_by("case_num")
        return cases

    def get_result_value(self, result):
        """Return the value of a result."""
        return str(result.case_num)

class CaseFormBasicView(FormView):
    form_class = CaseFormBasic
    template_name = "to_field_name/case_list.html"

    def get_initial(self):
        return {"cases": self.request.GET.get("cases", None)}

class CaseFormAutocompleteView(FormView):
    form_class = CaseFormAutocomplete
    template_name = "to_field_name/case_list.html"

    def get_initial(self):
        return {"cases": self.request.GET.get("cases", None)}
