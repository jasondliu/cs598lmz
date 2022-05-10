import mmap
import sys

#
#   Implements an additional command line argument -map
#   If it's given, the whole contents of a file will be mapped within
#   a single array. The array will be printed out in the same way
#   as regular arrays.
#
def dump_mapped_file(buf, p, end):
    print('[')
    for i in range(len(buf)):
        if i == 0:
            print('  ', end='')
        elif i % 16 == 0:
            print('\n  ', end='')
        print('%02x' % buf[i], end='')
        if i == len(buf) - 1:
            print(']')
        else:
            print(',', end='')

#
#   Prints help message
#
def print_help():
    print('''Usage: %s [OPTIONS] [FILE]

Prints raw data from a given file in a form of C arrays. Works like 'od -t x1 -An'.

Options:

  -
