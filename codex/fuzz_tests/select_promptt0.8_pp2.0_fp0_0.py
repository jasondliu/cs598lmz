import select
# Test select.select()
import queue
import time as timer
import threading
from ws4py.client.threadedclient import WebSocketClient
import json
from datetime import datetime

algorex_url = "wss://algorex-demo.algorex.tech"


class AlgorexWS(WebSocketClient):
    def __init__(self, client_id, api_key, event_delegate=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.api_key = api_key
        #self.queue = input_queue
        self.event_delegate = event_delegate
        self.timestamp = str(datetime.now().timestamp())

    def opened(self):
        print("Socket Opened")
        auth_msg = {
            "type": "auth",
            "client_id": self.client_id,
            "api_key": self.api_key,
            "timestamp": self.timestamp
        }
       
