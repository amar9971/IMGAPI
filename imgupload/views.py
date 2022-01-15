from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from rest_framework.views import APIView

from .serializer import ProfileSerializer

from .models import Profile


# Create your views here.
class ProfileImage(APIView):
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'massage': 'done'})
        return Response(serializer.errors)


    def get(self, request):
        data = Profile.objects.all()
        serializer = ProfileSerializer(data, many=True)
        return Response(serializer.data)
