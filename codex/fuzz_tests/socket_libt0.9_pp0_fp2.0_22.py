import socket
import sys
import time

from spycam import config
from spycam.client.client import StreamClient
from spycam.client.log import clearConsole
from spycam.client.log import log
from spycam.client.monitor import displayPic, getFps
from spycam.client.peers import PeerMonitor


class StreamClientApp:

    """Framework for a client application. Supporting a peer-to-peer video
    stream.

    Engine of a stream client application.

    """

    def __init__(self, clientIP, serverIP, streamPort=5005, heartbeatPort=5006,
                 heartbeatInterval=0.5, connectionTimeout=10, imageName='img',
                 clientName="pi", bufferSize=1024, verbosity=0):
        """*heartbeatPort* is for receiving heartbeats.

        *imageName* allows for testing different processing speeds and
        performance.

        """
        self.clientIP = clientIP
        self.serverIP = serverIP
        self.streamPort = streamPort
        self.heartbeatPort = heartbeatPort
        self.heartbeat
