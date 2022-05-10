import threading
threading._DummyThread._Thread__stop = lambda x: 42


import time

#from MyLoop import MyLoop

from twisted.internet import (
    reactor,
    ssl,
    task,
)


PUSH_URL = "wss://push.planetside2.com/streaming?environment=ps2&service-id=s:thorhammer"


class YourSimpleClientProtocol(WebSocketClientProtocol):


    def ping(self):
        print("ping")
        WebSocketClientProtocol.ping(self, "ping")

    def onMessage(self, _, payload, isBinary):
        print("receieved: {0}".format(payload))


def now():
    return int(time.time() * 1000)


class PingLoop(Task):

    def __init__(self):
        Task.__init__(self)
        self.protocol = None
        self.last_ping = now()

    def set_protocol(self, p):
        self.protocol = p

