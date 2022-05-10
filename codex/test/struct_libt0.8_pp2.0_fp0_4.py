import _struct

from encryption import pad16, unpad16
from errors import InvalidChecksum


__all__ = ['Packet']


class Packet(object):
    __slots__ = ['version', 'seq_no', 'length', 'checksum', 'data', 'checksum_source', 'header']

    def __init__(self, version, seq_no, payload, checksum_source=None):
        if not checksum_source:
            checksum_source = os.urandom(16)

        self.version = version
        self.seq_no = seq_no
        self.data = payload
        self.length = len(self.data) + 1
        self.checksum_source = checksum_source
        self.checksum = self.generate_checksum()

        self.header = struct.pack('>HI', (version << 14) + self.length, self.seq_no)

    @classmethod
    def parse(cls, packet_bytes, checksum_source=None):
        if len(packet_bytes) < 6:
            raise Value
