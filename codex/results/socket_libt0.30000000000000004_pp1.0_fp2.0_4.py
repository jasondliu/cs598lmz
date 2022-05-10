import socket
import time
import threading
import random
import sys

# Global Variables

# The port on which to listen
listenPort = 12000

# The port on which to send
sendPort = 12001

# The IP address of the server
serverIP = "127.0.0.1"

# The port on which to send to the server
serverPort = 12002

# The IP address of the client
clientIP = "127.0.0.1"

# The port on which to send to the client
clientPort = 12003

# The number of packets to send
numPackets = 10

# The maximum number of bytes in a packet
maxPacketSize = 1024

# The probability of a packet being dropped
dropProbability = 0.2

# The probability of a packet being corrupted
corruptProbability = 0.2

# The probability of a packet being delayed
delayProbability = 0.2

# The maximum delay time
maxDelayTime = 5

# A list of packets to be sent
packetsToSend = []

#
