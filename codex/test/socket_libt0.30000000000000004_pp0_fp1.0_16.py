import socket
import sys
import time
import threading
from threading import Thread
from threading import Lock
import Queue
import random
import json
import os
import signal

# Global variables
# The port number to listen on
listenPort = 0
# The hostname of the server
serverHostname = ""
# The port number of the server
serverPort = 0
# The number of clients
numClients = 0
# The number of requests per client
numRequests = 0
# The number of requests that have been sent
numRequestsSent = 0
# The number of requests that have been received
numRequestsReceived = 0
# The number of requests that have been failed
numRequestsFailed = 0
# The number of requests that have been succeeded
numRequestsSucceeded = 0
# The time that the first request was sent
firstRequestSentTime = 0
# The time that the last request was received
lastRequestReceivedTime = 0
# The total time that has been spent waiting for responses
totalResponseTime = 0
# The total time that has been spent waiting for responses
totalRequestTime = 0

