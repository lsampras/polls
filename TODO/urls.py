from django.urls import path

from . import views

app_name = 'TODO'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:todo_id>/update/', views.update, name='update'),
    path('<int:todo_id>/delete/', views.delete, name='delete'),
]