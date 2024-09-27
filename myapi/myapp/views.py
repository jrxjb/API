from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken 
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer,LoginSerializer, RegisterSerializer
from .baseView import BaseView


class RegisterView(BaseView,generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        if request.method != 'POST':
            return Response({'detail': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().post(request, *args, **kwargs)

class LoginView(BaseView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class LogoutView(BaseView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class TaskListCreateView(BaseView, generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Task.objects.all()

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskDetailView(BaseView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
