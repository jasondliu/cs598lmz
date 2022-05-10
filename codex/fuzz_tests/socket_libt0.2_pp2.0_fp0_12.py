import socket
import sys
import time
import threading
import Queue
import os

# Global Variables

# The port on which to listen for incoming data
listenPort = 5555

# The port on which to send data
sendPort = 5556

# The IP address of the server
serverIP = "127.0.0.1"

# The IP address of the client
clientIP = "127.0.0.1"

# The maximum size of a packet
maxPacketSize = 1024

# The maximum number of packets in a file
maxPackets = 100

# The maximum number of bytes in a file
maxBytes = maxPacketSize * maxPackets

# The maximum number of packets to send in a burst
maxBurst = 10

# The maximum number of packets to receive in a burst
maxBurstReceive = 10

# The maximum number of packets to send in a burst
maxBurstSend = 10

# The maximum number of packets to receive in a burst
maxBurstReceive = 10

# The maximum number of packets to send in a burst
maxBur
