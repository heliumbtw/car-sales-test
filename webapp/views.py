from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, status

from .models import Car
from .serializers import CarSerializer, UserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class CarList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def delete(self, request, format=None):
        users = Car.objects.all()
        if users:
            users.delete()
            return JsonResponse({'msg': 'Deleted successfully'}, status=status.HTTP_200_OK)
        return JsonResponse({'msg': 'Nothing to delete'}, status=status.HTTP_204_NO_CONTENT)


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Car
    serializer_class = CarSerializer
