from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.core.files.storage import default_storage
import requests
from django.contrib.auth import authenticate
from pdfminer.high_level import extract_text

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({'access': str(refresh.access_token)})
    return Response({'error': 'Invalid credentials'}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_resume(request):
    try:
        file = request.FILES['file']
    except KeyError:
        return Response({'error': 'No file uploaded'}, status=400)

    # Optionally save the file locally
    path = default_storage.save(file.name, file)

    # Send file to n8n webhook as multipart/form-data
    n8n_url = 'http://localhost:5678/webhook-test/resume'
    files = {'data': (file.name, file.file, file.content_type)}
    response = requests.post(n8n_url, files=files)

    return Response({'message': 'Uploaded successfully', 'n8n_response': response.text})

@api_view(['POST'])
def extract_pdf(request):
    try:
        file = request.FILES['file']
    except KeyError:
        return Response({'error': 'No file uploaded'}, status=400)

    try:
        text = extract_text(file.file)  # Pass file.file to extract_text
        return Response({'text': text})
    except Exception as e:
        return Response({'error': str(e)}, status=500)
