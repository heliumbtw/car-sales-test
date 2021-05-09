from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from webapp.views import CarList, CarDetail, UserCreate

urlpatterns = [
    path('cars/', CarList.as_view(), name='car-list'),
    path('cars/<str:pk>/', CarDetail.as_view(), name='car-detail'),
    path('account/register/', UserCreate.as_view()),
    path('api-token-auth/', obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
