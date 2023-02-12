from rest_framework import serializers

# Local 

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = (
            "id",
            "title",
            "body",
        )
