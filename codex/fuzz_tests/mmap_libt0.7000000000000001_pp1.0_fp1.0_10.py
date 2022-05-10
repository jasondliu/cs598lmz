import mmap
import struct
import hashlib

# TODO: try and make this work on both python 2.7 and 3.x


class gb_dram_map(object):
    """
    This class defines the Game Boy's DRAM map.

    It can be used to compare two ROMs that have the same code, but slightly
    different data. For example, the US and European versions of Super Mario
    Land.
    """
    def __init__(self):
        self.dram_map = {
            0x0000: 0x0150,
            0x0008: 0x0150,
            0x0010: 0x0150,
            0x0018: 0x0150,
            0x0020: 0x0150,
            0x0028: 0x0150,
            0x0030: 0x0150,
            0x0038: 0x0150,
            0x0040: 0x0150,
            0x0048: 0x0150,
            0x0050: 0x0150,
            0x0058:
