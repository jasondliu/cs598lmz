import mmap
import os
import shutil
import sys
import tempfile

from opcodes import *


def find_dcn(path):
    """
    Finds the file index of the .dcn file in a .bin file
    """
    # From: https://github.com/froop/Project-MUnT/blob/master/src/pmhax/hack.py#L187-L194
    with open(path, "rb") as f:
        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        offset = 0
        while True:
            if mm.read(1) == b"\x00":
                if mm.read(5) == b"pucku":
                    offset = mm.tell() - 6
                    break
            offset += 1
            mm.seek(offset)
    return offset


def align(value, alignment):
    if value % alignment == 0:
        return value
    return value + alignment - (value % alignment)


def write_asm(asm, fp):

