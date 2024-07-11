from django.urls import path

from profiles.views import ProfileListView, ProfileDetailView, ProfileCreateView


urlpatterns = [
    path('list', ProfileListView.as_view()),
    path('detail', ProfileDetailView.as_view()),
    path('', ProfileCreateView.as_view())
]
