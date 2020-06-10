from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.views import status
from rest_framework.response import Response
from api.models import Person
import re
from django.contrib.auth.hashers import check_password, make_password


class Update(APIView):
    def post(self, request):
        # This function is to execute updation of user details using the id they are given after Sign-in
        # The user-id is compulsorily accepted for retrieving that particular user's details.
        # The updated values are accepted for updation in the database.
        fname = request.data.get("fname")
        lname = request.data.get("lname")
        dob = request.data.get("dob")
        password = request.data.get("password")
        userid = request.user_id
        details = Person.objects.filter(userid=userid).first()
        if not details:
            return Response(
                {"Message": "User doesn't exist"}, status.HTTP_400_BAD_REQUEST
            )
        else:
            if not fname and not lname and not dob and not password:
                return Response(
                    {"Message": "Please fill the field you want to update"},
                    status.HTTP_400_BAD_REQUEST,
                )
            else:
                if fname:
                    details.fname = fname
                if lname:
                    details.lname = lname
                if dob:
                    details.userdob = dob
                if password:
                    details.password = make_password(password)
                details.save()
                return Response(
                    {"Message": "User details updated successfully!"},
                    status.HTTP_200_OK,
                )
