from django.urls import path
from .views import *
urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', MyObtainTokenPairView.as_view()),
    path('statistic/save/', SaveStatistics.as_view()),
    path('statistic/view/', ViewStatistics.as_view()),
    path('statistic/delete/<int:pk>/', DeleteStatistics.as_view())
]
