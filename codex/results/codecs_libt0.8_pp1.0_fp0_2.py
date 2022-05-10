import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

import requests
import json
import facebook
import datetime
import django.db.utils
import django.utils.timezone as timezone

from live_stream.models import LiveStream
from user_profile.models import UserProfile
import settings

app_id = settings.app_id
app_secret = settings.app_secret
long_lived_token = settings.long_lived_token

def get_long_lived_token():
    query_args = {'grant_type': 'fb_exchange_token', 'client_id': app_id, 'client_secret': app_secret, 'fb_exchange_token': long_lived_token}
    endpoint = "https://graph.facebook.com/oauth/access_token"
    response = requests.get(endpoint, params=query_args)
    if response.status_code == 200:
        data = json.loads(response.text)
        print data
        long_lived_
