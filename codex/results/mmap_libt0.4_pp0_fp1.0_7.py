import mmap
import os

def main():
    # Open a file
    fd = os.open( "foo.txt", os.O_RDWR )

    # Memory-map the file
    m = mmap.mmap( fd, 0 )

    # Read content via standard file methods
    print m.readline()

    # Update content using slice assignment
    m[6:] = 'world'

    # Close the map
    m.close()

    # Close the file
    os.close( fd )

if __name__ == '__main__':
    main()
