import _struct

from ctypes import *

PE_HEADER_OFFSET = 0x3C
PE_HEADER_OFFSET_64 = 0x3C

_IMAGE_DOS_HEADER = [
    ("e_magic", c_ushort),
    ("e_cblp", c_ushort),
    ("e_cp", c_ushort),
    ("e_crlc", c_ushort),
    ("e_cparhdr", c_ushort),
    ("e_minalloc", c_ushort),
    ("e_maxalloc", c_ushort),
    ("e_ss", c_ushort),
    ("e_sp", c_ushort),
    ("e_csum", c_ushort),
    ("e_ip", c_ushort),
    ("e_cs", c_ushort),
    ("e_lfarlc", c_ushort),
    ("e_ovno", c_ushort),
    ("e_res", c_ushort * 4),
    ("e_oemid", c_ushort
