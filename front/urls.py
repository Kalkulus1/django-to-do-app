from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="list"),
    # path('task-list/', views.taskList, name="task-list"),
    # path('task-show/<str:pk>/', views.taskShow, name="task-show"),
    # path('task-create/', views.taskCreate, name="task-create"),
    # path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    # path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]
