from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view

from api import serializers

@api_view(['GET'])
def userDetail(request,uuid=False):
    
    if uuid:
        try:
            user = User.objects.get(id=uuid)
            serializers = UserSerializer(user)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    else:
        users       = User.objects.all()
        serializers = UserSerializer(users, many=True)

    return Response(serializers.data)

@api_view(['POST'])
def userCreate(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def userUpdate(request,uuid):
    user = User.objects.get(id=uuid)
    serializer = UserSerializer(instance=user, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def userDelete(request,uuid):
    user = User.objects.get(id=uuid)
    user.delete()

    return Response(status=status.HTTP_200_OK)