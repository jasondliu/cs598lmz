import mmap
# Test mmap.mmap() features

def add_entities(mm):
    """
    Add some data to the mmap object
    
    @param mm - mmap object
    
    @return - nothing
    """
    mm.seek(0) # rewind
    num_entities = mm.read_byte()
    if num_entities == 0:
        mm.seek(0)
        mm.write_byte(1)
    else:
        mm.seek(0)
        mm.write_byte(num_entities+1)

def ring_test():
    """
    Testing ring buffer
    """
    # open file for writing, create if does not exist
    fd = os.open('myfile', os.O_RDWR | os.O_CREAT)
    # set file length
    os.write(fd, '\x00')
    # memory-map the file
    mm = mmap.mmap(fd, 4) # size of one message in ring buffer
    # Find out if mmap object is empty
    if mm.size == 4:
        print
