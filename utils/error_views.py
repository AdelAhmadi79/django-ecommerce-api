from django.http import JsonResponse
from rest_framework import status


def handler404(request, exception):
    massage = 'Route not found'
    response = JsonResponse(data={'error': massage})
    response.status_code = 404
    return response
def handler500(request):
    massage = 'Internal server error'
    response = JsonResponse(data={'error': massage})
    response.status_code = 500
    return response
