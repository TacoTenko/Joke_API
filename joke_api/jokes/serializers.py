from rest_framework import serializers
from .models import Joke

class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = '__all__'

    def validate_rating(self, value):
        """Ensure rating is between 1 and 5"""
        if value is not None and (value < 1 or value > 5):
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
