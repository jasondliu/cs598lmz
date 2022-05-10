import socket
socket.if_indextoname(3)

import os
import sys
import json
from pprint import pprint
from scapy.all import *
from zeroconf import ServiceBrowser, Zeroconf
from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.contrib.dns import DNSRR
from scapy.contrib.mqtt import MQTTPublish, MQTTSubscribe
from scapy.contrib.mqtt import MQTTConnect, MQTTConnectAck, MQTTDisconnect, MQTTDisconnectAck, MQTTPubcomp, MQTTPuback, MQTTPubrec, MQTTPubrel, MQTTSubscribe, MQTTSuback, MQTTSubunsuback, MQTTPing
from scapy.contrib.mqtt import MQTTPingreq, MQTTPingresp, MQTTUnsubscribe, MQTTUn
