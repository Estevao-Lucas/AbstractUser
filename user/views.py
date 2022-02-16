from rest_framework import viewsets
from user.permissions import UserPermission
from .models import User
from .serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_class = [TokenAuthentication]
    permission_classes = [UserPermission]
