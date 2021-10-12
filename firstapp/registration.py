from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
@api_view(['POST',])
def registration(request):
    if request.method=="POST":
        username=request.data['username']
        email=request.data['email']
        password1=request.data['password1']
        password2=request.data['password2']
        first_name=request.data['first_name']
        last_name=request.data['last_name']
        if password2 != password1:
            return Response({"error":"two password don't matched"})
        if User.objects.filter(username=username).exists():
            return Response({"error":"Username Already exists"})
        user = User()
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(raw_password=password1)
        user.is_active= True
        user.save()
        return Response({"success":"Successfully Registered"})
            