import weakref

from collections import defaultdict
from binascii import hexlify, unhexlify
from io import BytesIO

from xplane_constants import CONSTANTS, XPlaneVersionEnum, XPLErrorEnum, PacketIDEnum
from xplane_dataref_item import XPlaneDataRefItem
from xplane_dataref_writer import XPlaneDataRefWriter
from xplane_dataref_reader import XPlaneDataRefReader


class XPlaneConnect():
    def __init__(self,
                 in_host='127.0.0.1',
                 in_port=49000,
                 out_host='127.0.0.1',
                 out_port=49009,
                 ):
        self.input_host = in_host
        self.input_port = in_port
        self.output_host = out_host
        self.output_port = out_port
        self._transport = None
        self.loop = None
        self.callbacks = defaultdict(list)
        self.read
