import codecs
# Test codecs.register_error('surrogateescape', make_surrogateescape_error_handler)
# before you use these!
from gzip import open as gzip_open
from bz2 import open as bz2_open


import shutil
import errno
import stat


def cvt_hex_int(hex_str_upper):
    if not hex_str_upper.startswith("0x"):
        hex_str_upper = "0x" + hex_str_upper
    num = int(hex_str_upper, 0)
    return num


def cvt_int_hex(num, hex_dig=8):
    return "0x{0:0{1:d}X}".format(num, hex_dig)


def cvt_int_hex_pair(num, hex_dig=4):
    return "{0:0{1:d}X}".format(num, hex_dig)


def cvt_hex_int_pair_list(hex_str_upper):
    if not hex_str_upper.startswith("0x"):
