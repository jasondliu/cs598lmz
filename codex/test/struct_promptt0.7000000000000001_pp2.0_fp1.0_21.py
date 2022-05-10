import _struct
# Test _struct.Struct
import struct

SECTOR_SIZE = 512

def read_struct(fmt, fh, offset=None):
    size = struct.calcsize(fmt)
    if offset is not None:
        fh.seek(offset)
    data = fh.read(size)
    if len(data) != size:
        raise IOError
    return _struct.unpack(fmt, data)

def read_superblock(fh):
    superblock = read_struct('<2I8s8s8s8s8s8s8s8s8s8s8s8s8s8s', fh, offset=0x400)
    return superblock

def read_inode(fh, inode_index):
    # add 1 to inode index because inodes start at 1
    offset = (0x800 + (inode_index + 1) * 0x80)
    inode = read_struct('<2I2H2I2H4I2H2I2H2I', fh, offset=offset)
   
