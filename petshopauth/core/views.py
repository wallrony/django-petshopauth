from petshopauth.core.models import Pet
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from petshopauth.core.serializers import UserLoginSerializer, TokenSerializer, PetSerializer

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def list_or_add(request):
  if request.method == 'GET':
    pet_list = Pet.objects.all()

    serializer = PetSerializer(pet_list, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'POST':
    pet = PetSerializer(data=request.data)

    if pet.is_valid():
      pet.save()

      return Response(data=pet.data, status=status.HTTP_201_CREATED)
    return Response(data=pet.errors, status=status.HTTP_400_BAD_REQUEST)
  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def unique_pet(request, pet_id):

  try:
    pet = Pet.objects.get(id=pet_id)
  except Pet.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = PetSerializer(pet, many=False)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'PUT':
    serializer = PetSerializer(pet, request.data)

    if serializer.is_valid():
      serializer.save()

      return Response(serializer.data)
  elif request.method == 'DELETE':
    pet.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class UserLoginApiView(GenericAPIView):
  serializer_class = UserLoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)

    if serializer.is_valid():
      user = serializer.user
      token, _ = Token.objects.get_or_create(user=user)

      return Response(data=TokenSerializer(token).data, status=status.HTTP_200_OK)
    return Response({'message': 'authentication error'}, status=status.HTTP_400_BAD_REQUEST)