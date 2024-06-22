from rest_framework import serializers
from .models import *
from django.conf import settings

class MotoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required=False)
    class Meta:
        model = Moto
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        moto =super().create(validated_data)
        if image:
            moto.image_url = self.save_image(moto, image)
            moto.save ()
            return moto

    def save_image(self, moto, image):
        from django.core.files.storage import default_storage
        from django.core.files.base import ContentFile
        import os

        path = default_storage.save(os.path.join('image', str(moto.id) + '_'+ image.name), ContentFile(image.read()))
        return settings.MEDIA_URL + path

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class moto_marcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = moto_marca
        fields = '__all__'