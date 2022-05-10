import mmap, sys
from struct import pack, unpack

swapper = lambda x: x[1] or x[2]

size = (2048 + 512) * 512

def FDISK( offset, length ):
    return range(0, length) + range( (offset/512) * 512, offset )

def main():
    sector = 512
    
    # 'Fdisk' the disk
    root = 20*sector
    boot = FDISK( root, 10*sector )
    bootsect = FDISK( root, 1*sector )
    reserved = FDISK( root, 1*sector )
    
    
    dev = sys.argv[1]
    m = mmap.mmap(-1, size, dev,mmap.MAP_SHARED)
    

    
    # Step 1 - Replace the boot sector with a valid boot sector.
    for i in bootsect:
        m[i*512 : i*512+512] = [0] * 512
        
    m.seek(0*512)
    m.write(pack("8s8s
