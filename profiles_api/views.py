from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets


class HelloApiView(APIView):
    """Test API View """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get ,post,patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'hello world', 'an_apiview':an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handel a partial update pf an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk= None):
        """Delete an object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """ Return a hello method """
        a_viewset = [
        'Uses actions(list, create retrive update, partial_update)',
        'Automatically maps to URLs using Routers',
        'Provides more functionality with less code',
        ]

        return Response({'message':'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Helo {name}'
            return Response({'message': message})
        else:
             return Response(
            serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
             )
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID """
        return Response({'http_method':'GET'})

    def update(self, request, pk = None):
        """handel Updating an object """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk = None):
        """handel updating of an object"""
        return Response({'http_method':'Patch'})

    def destroy(self, request, pk=None):
        """handel remocing an object"""
        return Response({'http_method':'DELETE'})
