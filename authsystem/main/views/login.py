from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.views import status
from rest_framework.response import Response
from api.models import Person
from django.contrib.auth.hashers import check_password, make_password
import time
import datetime
import jwt


class Login(APIView):
    # This class is to execute the sign-up process which involves acceptig user details including
    # user email (this is checked for validity and whether this address exists in the database)
    # password (bcrypt is used to compare this password with the hashed password stored in the database)
    # Outputs include:
    # <Created 201>
    # {"Message": "Authentication successful!", "token": token}
    # (if the user exists in the database, a JWT token is generated using his user-id and shared with him)

    # <Bad request 400>
    # {"Message": "Fill the empty fields"}
    # (if any field is not filled)

    # <Bad request 400>
    # {"message": "User doesn't exist"}
    # (if the email is not in the database)

    # <Bad request 400>
    # {"message": "Invalid credentials"}
    # (if the passwords don't match)

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        if not email or not password:
            return Response({"message": "Enter all fields"}, status.HTTP_400_BAD_REQUEST)
        details = Person.objects.filter(useremail=email, flag=1).first()
        if details:
            if check_password(password, details.password):
                payload = {"userid": details.userid}
                token = jwt.encode(payload, "secret", algorithm="HS256")
                return Response({"message": "Signin succesful", "Token": token}, status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid email/password"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "User doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
