import mmap
# Test mmap.mmap.readline()

def main():
    # Open file
    fd = os.open('/tmp/mmaptest', os.O_CREAT|os.O_RDWR)

    # Zero out the file to insure it's the right size
    assert os.write(fd, '\x00'*1024) == 1024

    # Create the mmap insta
