from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title','author','barcode','status','issued_to','issue_date','return_date')

    def create(self,validated_data):
        return Book.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.barcode = validated_data.get('barcode', instance.barcode)
        instance.status = validated_data.get('status', instance.status)
        instance.issued_to = validated_data.get('issued_to', instance.issued_to)
        instance.issue_date = validated_data.get('issue_date', instance.issue_date)
        instance.return_date = validated_data.get('return_date', instance.return_date)
        instance.save()
        return instance
