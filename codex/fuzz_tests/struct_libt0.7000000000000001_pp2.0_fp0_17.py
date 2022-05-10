import _struct

from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol


class Sender(DatagramProtocol):
    def startProtocol(self):
        # Called when transport is connected
        pass

    def stopProtocol(self):
        # Called when transport is disconnected
        pass

    def datagramReceived(self, data, (host, port)):
        # called when datagram is received
        if data == 'ping':
            self.transport.write('pong', (host, port))


if __name__ == '__main__':
    # Set up API
    api = API('10.0.0.3', '10.0.0.2')

    # Set up receiver
    receiver = Receiver(api)

    # Set up sender
    sender = Sender()

    # Set up UDP receiver
    reactor.listenUDP(0, receiver)

    # Set up UDP sender
    reactor.listenUDP(0, sender)

    # Run API
    reactor.run()
