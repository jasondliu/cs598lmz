import threading
threading.get_ident

import json
import requests
import hmac
import hashlib
import inspect
import time
import logging
import math
import smtplib

from forex_signal_app_db import ForexSignalAppDB


class PoloniexLib:

    def __init__(self):
        self.URL = "https://poloniex.com/tradingApi"
        self.sessionpol = requests.session()
        self.sessionpol.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'})

    def api_query(self, command, req={}):
        if(command == "returnTicker" or command == "return24hVolume"):
            ret = requests.get(self.URL)
            return json.loads(ret.text)
