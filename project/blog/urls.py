

from django.urls import path
from . import views



urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:slug>', views.details, name='post-detail'),
    path('<slug:slug>/', views.category, name='category-detail'),

]
