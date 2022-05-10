import mmap
import struct
import pdb
import random
import math


def calc_mean(filename,output_file):
    ######################
    # Calculate the mean of the file
    ######################
    # get size of the file in bytes
    filesize = os.path.getsize(filename)

    # get size of the binary data in the file
    # to do so, we need to know the size of
    # the number we are reading (in this case, 4 bytes)
    bytes_per_number = 4

    # get the number of numbers in the file
    number_of_numbers = filesize / bytes_per_number

    # calculate the mean
    mean = 0

    # open the file
    with open(filename, "rb") as f:
        # open the file as a memory-mapped binary file
        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

        # read in the bytes and advance the pointer
        # read() takes the number of bytes to read and
        # returns a Python byte string.
