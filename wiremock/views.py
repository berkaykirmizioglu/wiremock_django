import requests
from django.http import JsonResponse
from .models import WiremockStub


def sync_with_wiremock(request):
    wiremock_url = "http://wiremock:8080/__admin/mappings"
    stubs = WiremockStub.objects.all()

    for stub in stubs:
        payload = {
            'request': stub.request,
            'response': stub.response
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(wiremock_url, json=payload, headers=headers)

        if response.status_code != 201:
            return JsonResponse({'status': 'failed', 'message': 'Error syncing with Wiremock'}, status=500)

    return JsonResponse({'status': 'success', 'message': 'Successfully synced with Wiremock'})