from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.core.files.storage import default_storage
import requests

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username == 'testuser' and password == 'testpass':
        token = RefreshToken.for_user(request.user)  # fake, so use dummy token
        return Response({'access': str(token.access_token)})
    return Response({'error': 'Invalid credentials'}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_resume(request):
    file = request.FILES['file']
    path = default_storage.save(file.name, file)
    # Call n8n webhook
    requests.post(
        'https://your-n8n-domain.com/webhook-url',
        json={'filename': file.name, 'filepath': path}
    )
    return Response({'message': 'Uploaded and sent to n8n'})
