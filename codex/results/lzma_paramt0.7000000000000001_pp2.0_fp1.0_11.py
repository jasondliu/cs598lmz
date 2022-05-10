from lzma import LZMADecompressor
LZMADecompressor()
from lzma import open as lzmaOpen

from ..tcp_connection import TCPConnection
from ..constants import *
from ..utils import *

from . import *

from . import _minecraft_packets as packets
from . import _minecraft_packets as packetsIn
from . import _minecraft_packets as packetsOut

MinecraftConnection = TCPConnection

class MinecraftConnection(TCPConnection):
    def __init__(self, *args, **kwargs):
        super(MinecraftConnection, self).__init__(*args, **kwargs)
        self.compressor = None

    def _handle_packet(self, packet):
        """
        Handles an incoming packet
        """
        self.logger.debug("Received packet: %s" % packet)
        if packet.id in self.packet_handlers:
            self.packet_handlers[packet.id](packet)

    def handle_packet(self, packet):
        """
        Handles the packet
        """
        if self.state == STATE_PLAY:
            self._
