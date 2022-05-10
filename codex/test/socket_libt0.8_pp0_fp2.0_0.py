import socket
import threading

from loguru import logger

from .model import Peer, PeerConnection

# ConnectToPeerThread
#
# A thread that connects to a peer.
#
# It waits for a short period of time (until it is sure that the main thread
# will not send any more messages to it). Then it connects to the peer,
# and then it exits.
#
# TODO: if it fails to connect, we would like to queue it again and retry
#       but we can't do that now since the socket is not ready and if an
#       error occurs, the thread will just exit (see Terminate()).
#
class ConnectToPeerThread(threading.Thread):
    def __init__(self, peer, listener, callback, terminate=None):
        super().__init__()
        self._peer = peer
        self._listener = listener
        self._callback = callback
        self._terminate = terminate

    def run(self):
        self._listener.IncreaseThreads()
        connection = None

