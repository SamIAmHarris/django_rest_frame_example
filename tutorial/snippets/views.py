from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status, generics, mixins, permissions, renderers, viewsets

from . import permissions as custom_permissions
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

"""
Implement our user api views with ViewSets
"""
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Auto provides list and detail actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

"""
Implement our api views with just generics
"""

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides list, create, retrieve,
    update, and destroy actions.

    Additionally we also provide an extra highlight action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, custom_permissions.IsOwnerOrReadOnly)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
