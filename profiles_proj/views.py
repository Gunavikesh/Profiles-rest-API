
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPiView(APIView):
    "Test API View"
    def get(self,request,format= None):
        """Returns a list of API view"""

        an_apiview=[
        'Uses HTTP methods as function (get,post,patch,put, delete)',
        'is similar to a traditional django view',
        'Gives you the most control over you appication logic',
        'is manually mapped to urls'
        ]
        return Response({'message': 'Hello !','an_apiview':an_apiview})
