from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .validators import validate_register_user


def register_user(request):
    """
    Register a user
    """
    # Validate request
    result = validate_register_user(request.data)
    if not result['is_valid']:
        response = {'message': 'Invalid values',
                    'errors': result['errors'], 'status': 400}
        return Response(response, status=400)

    # Create user
    try:
        user = User.objects.create_user(
            username=request.data['username'], email=request.data['email'], password=request.data['password'])
    except:
        response = {'message': 'An error occured', 'status': 400}
        return Response(response, status=400)

    # Generate JWT tokens
    tokens = RefreshToken.for_user(user)

    response = {'message': 'User successfully registered', 'data': {
        'access': str(tokens.access_token), 'refresh': str(tokens)}, 'status': 201}
    return Response(response, status=201)


def login(request):
    """
    Log a registered user in
    """
    email = request.data.get('email', None)
    password = request.data.get('password', None)

    user = authenticate(email=email, password=password)
    if not user:
        response = {'message': 'Invalid credentials', 'status': 400}
        return Response(response, status=400)

    tokens = RefreshToken.for_user(user)

    response = {'message': 'User successfully logged in', 'data': {
        'access': str(tokens.access_token), 'refresh': str(tokens)}, 'status': 201}
    return Response(response, status=201)
