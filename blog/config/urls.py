from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.home, name='index'),
    # ex: /polls/5/
    path('about/', views.about, name='about'),
    path('work/', views.work, name='work'),

    path('<int:entry_id>/', views.entry_detail, name='detail'),
    path('/<int:id>', views.entries, name='entries'),

]