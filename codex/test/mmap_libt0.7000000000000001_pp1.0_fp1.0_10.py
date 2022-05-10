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
