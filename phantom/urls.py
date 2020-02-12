from django.urls import path
from phantom.views import IndexPageView, IndexDetailView
from .views import get_form_data

app_name = 'phantom'

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('<str:slug>/', IndexDetailView.as_view(), name='ad_detail'),
    path('success/', get_form_data, name='form_data'),
]