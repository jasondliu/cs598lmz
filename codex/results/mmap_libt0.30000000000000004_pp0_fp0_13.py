import mmap
import sys
import os

#
#
#
def main():
    if len(sys.argv) != 2:
        print "Usage: %s <filename>" % sys.argv[0]
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print "File %s does not exist" % filename
        sys.exit(1)

    #
    # Open the file
    #
    f = open(filename, "r+")

    #
    # Memory map the file
    #
    m = mmap.mmap(f.fileno(), 0)

    #
    # Read the first line
    #
    line = m.readline()
    print "First line: %s" % line

    #
    # Move to the end of the file
    #
    m.seek(0, os.SEEK_END)

    #
    # Write the rest of the file
    #
    m.write("\nThis is the last line of the file\n")
