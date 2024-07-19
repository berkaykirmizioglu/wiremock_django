import requests
from django.db import models
from django.contrib.postgres.fields import JSONField


class WiremockStub(models.Model):
    name = models.CharField(max_length=100)
    request = JSONField()
    response = JSONField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.sync_with_wiremock()

    def sync_with_wiremock(self):
        wiremock_url = "http://wiremock:8080/__admin/mappings"
        payload = {
            'request': self.request,
            'response': self.response
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(wiremock_url, json=payload, headers=headers)
        if response.status_code != 201:
            raise Exception(f"Error syncing stub {self.name} with WireMock")