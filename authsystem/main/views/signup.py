from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.views import status
from rest_framework.response import Response
from api.models import Person
import re
from django.contrib.auth.hashers import check_password, make_password


# For checking email using regular expression
regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"


def check(email):
    if re.search(regex, email):
        return True
    else:
        return False


# Class for sign up. New user will register or make an account.
# Password is stored at backend in encrypted form using one way Bcrypt technique.


class Signup(APIView):
    def post(self, request):
        fname = request.data.get("fname")
        lname = request.data.get("lname")
        email = request.data.get("email")
        password = request.data.get("password")
        dob = request.data.get("dob")
        check1 = check(email)
        details = Person.objects.filter(useremail=email).first()
        if details:
            return Response({"message": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)
        if not fname or not lname or not password or not dob or not email:
            return Response({"message": "Please fill required fields"}, status=status.HTTP_400_BAD_REQUEST)
        elif not check1:
            return Response({"message": "Bad email"}, status=status.HTTP_400_BAD_REQUEST)
        password_hash = make_password(password)
        Person.objects.create(fname=fname, lname=lname, useremail=email, password=password_hash, userdob=dob)
        return Response({"result": "You've signed up sucessfully!"}, status.HTTP_200_OK)
