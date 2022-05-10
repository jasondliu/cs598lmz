import threading
# Test threading daemon with process that POST xml to current endpoint
# @author: Michael Muzzio

# Test an XML response to send to device
# Test from the server
from Crypto.Hash import SHA256

from datetime import datetime
import json
from SignalAcquirer import RSA_KEY
import socket
from xml.dom.minidom import parseString
import xml.dom
from xml.dom.minidom import parse, parseString

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_PATH, '../../lib'))
from topo_msg import Topo_Msg
from response_msg import Response_Msg
from SensorFirewall import DeviceData
from SensorFirewall import UpdateHandler

# Generate a topo message to send to the device
def generate_topo_msg_xml(self):
    request_msg = '<?xml version=\"1.0\"?> \
        <?xml-stylesheet type=\"text/xsl\" href=\"/NetFED/tradefed/style/sn
