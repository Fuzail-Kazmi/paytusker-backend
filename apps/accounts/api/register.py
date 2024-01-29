from rest_framework.views import APIView
from apps.accounts.models import User
from django.core.validators import validate_email
from django.http import HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework import status


class RegisterUser(APIView):
    def post(self, request):
        user_object = request.data
        user_object = self.validate_user_object(user_object)

        if self.validate_email(user_object.get("email")):
            return Response(data="Email is not vaild", status=status.HTTP_403_FORBIDDEN)

        # user = User.objects.create(
        #     first_name=user_object.get("first_name"),
        #     last_name=user_object.get("last_name"),
        #     username=user_object.get("username"),
        #     password=user_object.get("password"),
        #     email=user_object.get("email"),
        #     phone_number=user_object.get("phone_number"),
        # )

        # user.save()
        # from apps.store.models.customer import Customer

        # if user:
        #     Customer.objects.create(
        #         user=user, customer_name=f"{user.first_name} {user.last_name}"
        #     )
        return Response({"message": "user registered"}, status=200)

    def validate_user_object(self, user_object: dict):
        required_fields = [
            "first_name",
            "last_name",
            "username",
            "phone_number",
            "email",
            "password",
        ]

        # for key in user_object.items():
        #     if key not in required_fields:
        #         return Response(data=f"{key} is missing")

        if not self.validate_email(user_object.get("email")):
            return Response(data="email is not vaild")

        return user_object

    def validate_email(self, email):
        "first we have validate email with RE"

        user = User.objects.filter(email=email)

        if user:
            return True

        return False
