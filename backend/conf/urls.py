from django.urls import path, include

urlpatterns = [
    path('profiles/', include('profiles.urls')),
]
