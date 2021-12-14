from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import Statistic



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class SaveStatistics(generics.CreateAPIView):
    queryset = Statistic.objects.all()
    serializer_class = SaveStatisticsSerializer
    permission_classes = (IsAuthenticated, )
class ViewStatistics(generics.ListAPIView):
    def get_queryset(self):
        from_date = self.request.data['from']
        to_date = self.request.data['to']
        if 'order' in self.request.data:
            return Statistic.objects.all().filter(date__gte=from_date, date__lte=to_date).order_by(self.request.data['order'])
        else:
            return Statistic.objects.all().filter(date__gte=from_date, date__lte=to_date).order_by('date')

    serializer_class = StatisticsSerializer
    permission_classes = (IsAuthenticated, )

class DeleteStatistics(generics.DestroyAPIView):
    serializers = StatisticsSerializer
    def get_queryset(self):
        return Statistic.objects.all().filter(id=self.kwargs['pk'])
    permission_classes = (IsAuthenticated, )