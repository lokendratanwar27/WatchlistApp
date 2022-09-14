from multiprocessing.dummy import active_children
from unicodedata import name
from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    Description = serializers.CharField()
    active = serializers.BooleanField()
    
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.Description = validated_data.get('description',instance.Description)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance
    
        
    