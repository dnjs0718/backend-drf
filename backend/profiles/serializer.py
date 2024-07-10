from enum import StrEnum

from rest_framework import serializers
from profiles.models import Profile


class ProfileListOrderingEnum(StrEnum):
    NAME_ASC = "name"
    NAME_DESC = "-name"
    EMAIL_ASC = "email"
    EMAIL_DESC = "-email"
    TEL_ASC = "tel"
    TEL_DESC = "-tel"


class ProfileOrderingSerializer(serializers.Serializer):
    ordering = serializers.ChoiceField(choices=[e.value for e in ProfileListOrderingEnum], required=False)


class ProfileListSerializer(serializers.ModelSerializer):
    labels = serializers.SerializerMethodField()
    company = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id',
            'img_url',
            'name',
            'email',
            'tel',
            'rank',
            'company',
            'labels'
        ]

    def get_labels(self, obj):
        return obj.labels.values_list('name', flat=True)
    

class ProfileDetailSerializer(serializers.ModelSerializer):
    labels = serializers.SerializerMethodField()
    company = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id',
            'img_url',
            'name',
            'email',
            'tel',
            'rank',
            'company',
            'labels',
            'memo',
            'address',
            'birthday',
            'web_site'
        ]

    def get_labels(self, obj):
        return obj.labels.values_list('name', flat=True)