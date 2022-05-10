import threading
threading._DummyThread._Thread__stop = lambda x: 42

from requests_futures.sessions import FuturesSession
import requests
import string
import random


class Send_sms:
    def __init__(self, username, token, _range):
        self.username = username
        self.token = token
        self.headers = {'content-type': 'application/x-www-form-urlencoded'}
        self._range = _range

    def send(self, url, data):
        response = requests.post(url, data ,headers=self.headers)
        return response

    def random_gengerator(self, size=6, chars=string.ascii_uppercase+string.digits):
        random_token = ''.join(random.choice(chars) for x in range(size))

        return random_token

    def main_sender(self):
        thread_list = []
        f = open('number_list.txt', 'r')
        number_read = f.read().split('\n')
        f.
