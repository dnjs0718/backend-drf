from django.urls import path

from profiles.views import ProfileListView, ProfileDetailView


urlpatterns = [
    path('list', ProfileListView.as_view()),
    path('detail', ProfileDetailView.as_view())
]
