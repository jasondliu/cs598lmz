import mmap
import os
import re
import subprocess
import sys
import tempfile

from optparse import OptionParser


def main():
    usage = "usage: %prog [options] [input_file] [output_file]"
    parser = OptionParser(usage=usage)
    parser.add_option("-s", "--start", dest="start_address",
            help="start address of memory map",
            default=None)
    parser.add_option("-e", "--end", dest="end_address",
            help="end address of memory map",
            default=None)
    parser.add_option("-p", "--permission", dest="permission",
            help="permission of memory map",
            default="rw-")
    parser.add_option("-o", "--offset", dest="offset",
            help="offset of memory map",
            default=0)
    parser.add_option("-d", "--data", dest="data",
            help="data to write to memory",
            default=None)
