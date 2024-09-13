from django.urls import path
from .views import RegisterView, LoginView, LogoutView, TaskListCreateView, TaskDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/datails/', TaskDetailView.as_view(), name='task-detail'), 
]



