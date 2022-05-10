import socket
import time
import sys
import os
import threading

# This is the port number that the server is listening on
serverPort = 12000

# This is the IP address of the server
serverIP = '127.0.0.1'

# This is the size of the buffer used to receive data from the server
bufferSize = 1024

# This is the number of seconds the client will wait for a response from the server
timeout = 10

# This is the number of seconds the client will wait before sending a keep alive message
keepAlive = 5

# This is the number of seconds the client will wait before sending a keep alive message
keepAliveInterval = 5

# This is the number of seconds the client will wait before sending a keep alive message
keepAliveCount = 3

# This is the number of seconds the client will wait before sending a keep alive message
keepAliveTimeout = 5

# This is the number of seconds the client will wait before sending a keep alive message
keepAliveRetry = 5

# This is the number of seconds the client will wait before sending a keep alive message
keepAl
