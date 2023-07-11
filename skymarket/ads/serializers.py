from phonenumber_field import serializerfields
from rest_framework import serializers

from ads.models import Comment, Ad


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="author.id")
    author_first_name = serializers.ReadOnlyField(source="author.author_first_name")
    author_last_name = serializers.ReadOnlyField(source="author.author_last_name")
    ad_id = serializers.ReadOnlyField(source="ad.id")

    class Meta:
        model = Comment
        fields = ("pk", "text", "created_at", "author_id", "author_first_name", "author_last_name", "ad_id")


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "description")


class AdDetailSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="author.id")
    author_first_name = serializers.ReadOnlyField(source="author.author_first_name")
    author_last_name = serializers.ReadOnlyField(source="author.author_last_name")
    phone = serializerfields.PhoneNumberField(source="author.phone", read_only=True)
    class Meta:
        model = Ad
        fields = ("pk", "title", "price", "description", "phone", "image",
                  "author_id", "author_first_name", "author_last_name")
