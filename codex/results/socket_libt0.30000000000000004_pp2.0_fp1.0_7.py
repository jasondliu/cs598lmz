import socket
import sys
import time
import os
import threading
import random
import string
import json
import base64

# This is the port that the server is listening on
serverPort = 12000

# This is the port that the client is listening on
clientPort = 12001

# This is the IP address of the server
serverIP = '127.0.0.1'

# This is the IP address of the client
clientIP = '127.0.0.1'

# This is the maximum size of a packet
maxPacketSize = 1024

# This is the timeout value for the server
timeout = 10

# This is the maximum number of packets that can be sent in a row
maxPackets = 10

# This is the maximum number of packets that can be sent in a row
maxPackets = 10

# This is the number of packets that have been sent
packetsSent = 0

# This is the number of packets that have been received
packetsReceived = 0

# This is the number of packets that have been dropped
packetsDropped = 0

# This is
