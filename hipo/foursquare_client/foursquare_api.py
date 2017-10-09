import json, requests
from django.conf import settings

class FoursquareSearchRequest(object):

    def __init__(self):
        self.client_id = getattr(settings, 'FOURSQUARE_CLIENT_ID', '')
        self.client_secret = getattr(settings, 'FOURSQUARE_CLIENT_KEY', '')
        self.url = getattr(settings, 'FOURSQUARE_VENUES_SEARCH', '')
        self.version = getattr(settings, 'FOURSQUARE_VERSION', '')

    def getVenuesInfo(self, query, near):
        params = dict(
            client_id = self.client_id,
            client_secret = self.client_secret,
            v = self.version,
            query= query,
            near= near
        )

        resp = requests.get(url=self.url, params=params)
        data = json.loads(resp.text)

        return data