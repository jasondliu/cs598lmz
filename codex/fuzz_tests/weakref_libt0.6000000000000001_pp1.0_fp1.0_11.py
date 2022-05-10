import weakref

from twisted.internet.defer import inlineCallbacks
from twisted.internet.error import ConnectionDone
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver


class LineProtocol(LineReceiver):
    def __init__(self):
        self.__commands = {}
        self.__pending_responses = {}
        self.__seq = 0

    def lineReceived(self, line):
        try:
            self.__handle_line(line)
        except Exception:
            self.transport.loseConnection()

    def __handle_line(self, line):
        if line.startswith("!"):
            self.__handle_response(line)
        elif line.startswith("?"):
            self.__handle_command(line)
        else:
            raise ValueError("Unknown line type: %s" % line)

    def __handle_response(self, line):
        seq_str, response = line[1:].split(" ", 1)
        seq_num = int(seq_
