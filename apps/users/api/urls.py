from django.urls import path
from apps.users.api.views.general_views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]