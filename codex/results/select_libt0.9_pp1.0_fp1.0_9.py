import select
import socket
import sys
import threading
import time
import traceback

from server import Server

# Hosts a local metalog port that only accepts connections from
# localhost so that users with a malicious metalog can't mess with
# the server files.

class LocalServer(Server):
    def __init__(self, metalog):
        Server.__init__(self, 7276, metalog)
        if self.bind(("127.0.0.1",), True, False) != None:
            print("Couldn't connect to metalog, please try again later.")
            sys.exit(1)

        # Launch thread to listen for connections.
        class DummyThread(threading.Thread):
            def run(self):
                self.run_start()
            def run_start(self):
                self.listen_for_connections()

        self.listenThread = DummyThread();
        assert self.listenThread != None

        self.listenThread.start()

        # Wait for the thread to start before we exit.
        while not self.started
