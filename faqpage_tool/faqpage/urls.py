# faqpage/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.faq_list, name='faq_list'),
    path('edit/<int:faq_id>/', views.edit_faq, name='edit_faq'),
    path('delete/<int:faq_id>/', views.delete_faq, name='delete_faq'),
    path('view-schema/', views.view_schema, name='view_schema'),
]
