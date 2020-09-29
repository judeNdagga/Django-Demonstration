from rest_framework.views import APIView

from . import auth_crud


class RegisterUserAPIView(APIView):

    def post(self, request):
        return auth_crud.register_user(request=request)


class LogInUserAPIView(APIView):

    def post(self, request):
        return auth_crud.login(request=request)
