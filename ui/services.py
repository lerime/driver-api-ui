import requests
from django.conf import settings


class DriverService:
    base_url = settings.DRIVER_SERVICE_URL

    def get_all_records(self, params):
        endpoint = "drivers"
        url = f"{self.base_url}{endpoint}"
        response = self.make_request(url=url, params=params)
        return response['records']

    @staticmethod
    def make_request(method="GET", url=None, params=None, data=None):
        response = requests.request(method=method, url=url, json=params, data=data)
        response.raise_for_status()
        return response.json()
