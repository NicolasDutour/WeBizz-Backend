from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint to get users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
