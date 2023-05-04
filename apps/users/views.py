from rest_framework.generics import ListAPIView

from apps.users.models import User
from apps.users.serializer import UserSerializer
# Create your views here.
class UserAPIView(ListAPIView):
    queryset = User.objects.all() #SELECT * FROM users_user; Django ORM
    serializer_class = UserSerializer