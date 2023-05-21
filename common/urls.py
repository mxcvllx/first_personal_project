from django.urls import path

from common.views import CategoryListApiViews, ContactUsListApiView, AboutUsListApiViews

urlpatterns = [
    path('category/', CategoryListApiViews.as_view(), name='category'),
    path('contact-us/', ContactUsListApiView.as_view(), name='contact-us'),
    path('about-us/', AboutUsListApiViews.as_view(), name='about-us'),
]
