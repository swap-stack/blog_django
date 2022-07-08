from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.home, name='index'),
    # ex: /polls/5/
    path('<int:entry_id>/', views.entry_detail, name='detail'),

    path(r'^ajax/get_entries/$', views.entries, name='entries'),

]