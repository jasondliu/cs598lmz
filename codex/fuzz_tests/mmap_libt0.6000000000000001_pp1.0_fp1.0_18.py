import mmap
import os
import re

def usage():
    print("Usage: python3 {} [infile] [outfile] [min_length] [max_length]".format(
        sys.argv[0]))
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        usage()

    infile = sys.argv[1]
    outfile = sys.argv[2]
    min_length = int(sys.argv[3])
    max_length = int(sys.argv[4])

    with open(infile, 'r') as f:
        with open(outfile, 'w') as o:
            for line in f:
                line = line.strip()
                if re.match('.*(?P<min>{})'.format(min_length) +
                    '.*(?P<max>{})'.format(max_length) +
                    '.*', line):
                    o.write(line + '\n')
