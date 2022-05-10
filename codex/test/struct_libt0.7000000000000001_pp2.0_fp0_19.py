import _struct

from . import amf0
from . import amf3
from . import utils

class Packet:
    def __init__(self, header, body):
        self.header = header
        self.body = body

class PacketHeader:
    def __init__(self):
        self.size = 0
        self.type = 0
        self.stream_id = 0

class PacketBody:
    def __init__(self):
        self.decoder = None

class ConnectPacket:
    def __init__(self, transaction_id, command_object, optional_params=None, encoder_type=amf0.AMF0Encoder):
        self.transaction_id = transaction_id
        self.command_object = command_object
        self.optional_params = optional_params
        self.encoder_type = encoder_type

    def serialize(self):
        body_bytes = self.encoder_type.encode(self.command_object)

        if self.optional_params is not None:
            body_
