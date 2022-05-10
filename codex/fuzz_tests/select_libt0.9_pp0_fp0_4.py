import selectors
sys.path.insert(0, os.getcwd())
from coapthon.client.helperclient import HelperClient
from coapthon.messages.message import Message
from coapthon.messages.request import Request
from coapthon.messages.response import Response
from coapthon.client.coap_protocol import CoAP
import json


first_call = True
safe_values = []

def valid_json(json_content):
    try:
        json_object = json.loads(json_content)
    except:
        return False
    else:
        return True


class CoAPClient(CoAP):
    def __init__(self, serverip, serverport, multicast=False):
        CoAP.__init__(self, (serverip, serverport), multicast)

    def send_request(self, request):
        if self._stopped.is_set():
            raise RuntimeError("Client stopped")
        request.destination = (self._server_ip, self._server_port)
        if
