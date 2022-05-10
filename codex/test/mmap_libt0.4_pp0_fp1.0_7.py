import mmap
import os

def main():
    # Open a file
    fd = os.open( "foo.txt", os.O_RDWR )

    # Memory-map the file
    m = mmap.mmap( fd, 0 )

    # Read content via standard file methods
