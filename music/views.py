from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST', 'PUT', 'DELETE'])
def music_list(request):


    return Response('ok')
