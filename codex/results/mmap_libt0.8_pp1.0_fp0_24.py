import mmap
import struct
import sys
import time

from PIL import Image

# open memory device
fd = os.open( "/dev/mem", os.O_RDWR | os.O_SYNC )

# memory-map GPIO peripheral
mm = mmap.mmap( fd, GPIO_BLOCK_SIZE, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, offset=GPIO_BASE )

# define helper to set/clear GPIO bits
def set_bit( index, value ):
    reg = GPIO_DATA + ( index >> 5 ) * 4
    off = index & 31
    with mmap.mmap( fd, 4, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, offset=reg ) as buf:
        # read current register value
        data = struct.unpack( 'I', buf )[0]
        if value:
            # set bit
            data |= ( 1 << off )
        else:
            # clear bit
            data
