from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import Student

class studentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'