from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse


from .services.CIN_service import CIN
from .forms import CINForm

class CIN_View(View):
    form_class = CINForm
    template_name = 'CINExtract/cin.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        detailed_cin = "yeds"
        if form.is_valid():
            cin = form.cleaned_data['cin']
            detailed_cin = CIN(cin).get_details()
            print(detailed_cin)
            return HttpResponseRedirect(reverse('cin'))

        return render(request, self.template_name, {'form': form, 'form_data': detailed_cin })