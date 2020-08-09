from FTLapp.models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

## listing available userdata using viewset
class AccountViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        my_dict = {'ok': True, 'members':serializer.data}
        return Response(my_dict)

    # Adding Login authentication to the API
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    