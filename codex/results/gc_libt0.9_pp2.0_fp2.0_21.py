import gc, weakref

from .device import *
import htsworkflow.frontend.permissions
from htsworkflow.frontend.api_client import APIUser

class ClientConnection(object):
    """A connection (session) to the API

    For a given API URL and user it maintains information about
    the user's session and devices available.
    """
    def __init__(self, api_url, user):
        self.api_url = api_url
        self.apidev = APIUser(api_url)
        self.user = user
        self.username = user.username
        self.logged_in = False
        self.devices = weakref.WeakValueDictionary()
        self.socketio = None

    def __del__(self):
        print("ClientConnection deleted")

    def get_device(self, device_name):
        if device_name in self.devices:
            return self.devices[device_name]
        device = Device(device_name, self)
        self.devices[device_name] = device
        return device

    def login(self
