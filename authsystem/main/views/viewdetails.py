from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
import jwt
from rest_framework.response import Response
from api.models import Person
from rest_framework import viewsets


class Display(APIView):

    """This class is for the user to see their details which are retrieved from the database.
    On entering their JWT token (received during Sign-in), their user-id is decoded and they can get their details.
    Outputs received:
    <Bad request 400>
    {"Message": "Fill the empty fields"}
    (if any field is not filled)

    <Bad request 400>
    {"message": "User doesn't exist"}
    (if the userid is not in the database)

    <Created 201>
    {"Your details: First-name:": userdetails.fname, "Last-name:": userdetails.lname, "Date of birth:": 
    userdetails.userdob, "Email:": userdetails.useremail} """

    def get(self, request):

        userid = request.user_id
        userdetails = Person.objects.filter(userid=userid).first()
        if not userdetails:
            return Response(
                {"Message": "User doesn't exist"}, status.HTTP_400_BAD_REQUEST
            )
        else:
            return Response(
                {
                    "First-name:": userdetails.fname,
                    "Last-name:": userdetails.lname,
                    "Date of birth:": userdetails.userdob,
                    "Email:": userdetails.useremail,
                },
                status.HTTP_200_OK,
            )
