from rest_framework import serializers
from links.models import Link

class LinkSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    slug = serializers.CharField(required=True, max_length=100)
    clicks = serializers.IntegerField()

    def create(self, validatedFields):
        return Link.objects.create(slug=validatedFields.slug, clicks=0)

    def update(self, instance, validatedFields):
        instance.slug = validatedFields.slug
        instance.save()
        return instance