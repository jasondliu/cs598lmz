import mmap
# Test mmap.mmap vs. mmap.mmap_async
# In both cases, the problems goes away if we remove the mmap
# step and read the image directly from disk
#
# Would like to understand why mmap has a similar effect to memory
# allocation - in both situations vpython runs out of graphics
# context and stops redrawing
#
# In both cases, the problems goes away if we remove the mmap
# step and read the image directly from disk

# This is a memory-mapped image, 512 by 512 pixels, 3 bytes per pixel:
filename = 'C:\\Users\\Public\\Pictures\\Sample Pictures\\desert.jpg'

def mmap_image():
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print('mmap:', mm)
    return mm

def mmap_async_image():
    mm = mmap.mmap_async(f.fileno(), 0, access=mmap.ACCESS_READ)
    print('mmap_async:', mm)
    return mm


