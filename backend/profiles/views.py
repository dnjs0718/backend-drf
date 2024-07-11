from enum import StrEnum

from rest_framework import generics, pagination

from profiles.models import Profile
from profiles.serializer import (
    ProfileOrderingSerializer,
    ProfileListSerializer,
    ProfileDetailSerializer,
    ProfileCreateSerializer
)


class ProfileListOrderingEnum(StrEnum):
    NAME_ASC = "name"
    NAME_DESC = "-name"
    EMAIL_ASC = "email"
    EMAIL_DESC = "-email"
    TEL_ASC = "tel"
    TEL_DESC = "-tel"


class ProfileListPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100 
    
    
class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer
    pagination_class = ProfileListPagination

    def get_queryset(self):
        queryset = super().get_queryset().select_related('company')
        
        serializer = ProfileOrderingSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)

        ordering = serializer.validated_data.get('ordering', None)
        
        if ordering:
            queryset = queryset.order_by(ordering)
        
        return queryset


class ProfileDetailView(generics.RetrieveAPIView):
    serializer_class = ProfileDetailSerializer  

    def get_object(self):
        id = self.request.query_params.get('id')
        
        profile = generics.get_object_or_404(Profile, id=id)
        return profile


class ProfileCreateView(generics.CreateAPIView):
    serializer_class = ProfileCreateSerializer