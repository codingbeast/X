from rest_framework import serializers
from .models import details
class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = details
        fields = ('title', 'image', 'url', 'tag', 'videotype')
