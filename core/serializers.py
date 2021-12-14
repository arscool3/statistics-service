from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token


class SaveStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'

    def create(self, validated_data):
        date = validated_data['date']
        views = None
        clicks = None
        cost = None
        cpc = None
        cpm = None
        if 'views' in validated_data:
            views = validated_data['views']
        if 'clicks' in validated_data:
            clicks = validated_data['clicks']
        if 'cost' in validated_data:
            cost = validated_data['cost']

            if 'clicks' in validated_data:
                cpc = cost / clicks
            if 'views' in validated_data:
                cpm = cost / views * 1000

        statistic = Statistic.objects.create(date=date, views=views, clicks=clicks, cost=cost, cpc=cpc, cpm=cpm)
        return statistic


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'