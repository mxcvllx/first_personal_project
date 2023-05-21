from django.urls import path

from users.views import RegisterView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path("profile/", ProfileView.as_view(), name="profile"),
]
