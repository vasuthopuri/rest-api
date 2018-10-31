from rest_framework import serializers
from .models import User
from rest_framework import generics
from .Serializers import UserSerializer
from rest_framework import mixins
# model serializer [similar to forms.ModelForm]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "phone")

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()

    serializer_class = UserSerializer

class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#class UserDeleteView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    #queryset = User.objects.all()
    #serializers_class = UserSerializer
#def get(self, request, *args, **kwargs):
        #return self.destroy(request, *args, **kwargs)