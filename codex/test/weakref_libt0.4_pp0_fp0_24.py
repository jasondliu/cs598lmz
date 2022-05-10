import weakref

from spock.mcp import mcdata
from spock.mcp import mcpacket
from spock.mcp import nbt
from spock.mcp.mcpacket import Packet

from spock.utils import pl_announce

class PacketHandler:
    def __init__(self, sock, queue):
        self.sock = sock
        self.queue = queue
        self.buffer = b''
        self.state = mcdata.HANDSHAKE_STATE
        self.packet_handlers = {
            mcdata.HANDSHAKE_STATE: self.handshake_handler,
            mcdata.STATUS_STATE: self.status_handler,
            mcdata.LOGIN_STATE: self.login_handler,
            mcdata.PLAY_STATE: self.play_handler,
        }

    def handle(self):
        self.buffer += self.sock.recv(4096)
