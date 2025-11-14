import json

from django.views import View
from django.http import HttpRequest, JsonResponse

from .models import User


class AccountView(View):

    def post(self, request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body.decode())
        
        try:
            User.objects.get(username=data['username'])
            return JsonResponse(data={'message': 'user exists.'}, status=400)
        
        except User.DoesNotExist:
            user = User(
                username=data['username'],
                password=data['password'],
                email=data.get('email'),
                phone=data.get('phone'),
            )
            user.save()

            return JsonResponse(data={'message': 'user created.'}, status=201)


# signals
