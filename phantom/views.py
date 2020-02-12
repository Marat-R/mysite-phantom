from django.shortcuts import render
from phantom.models import Advertisement, ContactData
from django.views.generic import ListView, DetailView, FormView
from django.http import HttpResponse
from django.urls import reverse_lazy


# def get_form_data(request):
#     if request.method == 'POST':
#         print("ok")
#     return render(request, 'phantom/success.html', {})

class IndexPageView(FormView, ListView):
    template_name = 'phantom/index.html'
    model = Advertisement
    form_class = ContactDataForm
    context_object_name = 'advertisements'

    def get_queryset(self, *args, **kwargs):
        return Advertisement.objects.filter(active=True)


class IndexDetailView(DetailView):
    template_name = 'phantom/generic.html'
    model = Advertisement
    context_object_name = 'advertisement'
    form_class = ContactDataForm


