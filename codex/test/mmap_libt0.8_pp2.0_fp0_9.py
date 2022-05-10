import mmap
import string
import sys


def main(argv):
    if (len(argv) != 2):
        print('Usage: %s file' % argv[0])
        return 1

    if not os.path.exists(argv[1]):
        print('ERROR: File %s was not found!' % argv[1])
        return 1

    if not os.path.isfile(argv[1]):
        print('ERROR: %s is not a file!' % argv[1])
        return 1

    f = open(argv[1], 'r')
    map = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)

    count = 0
    total_num_words = 0
    print('String\t\t\tOccurrences')
    print('==============================')

    while True:
        w = []
        while True:
            c = map.read_byte()
