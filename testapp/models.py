from django.db import models
from rest_framework_json_api import serializers
from rest_framework_json_api import views

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=2000, blank=True)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CategoryViewSet(views.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filterset_field = ("id", "name",)
