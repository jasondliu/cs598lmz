import _struct
from enum import IntEnum, IntFlag, auto

from elftools.elf.elffile import ELFFile
from elftools.elf.descriptions import describe_symbol_type
from elftools.elf.dynamic import DynamicSection, DynamicSegment
from elftools.elf.constants import SH_FLAGS
import pyelftools.constants.linux as linux
import pyelftools.constants.elf as elf

from numpy import *
from numpy.linalg import *


class Elf:
    """Python wrapper class for an ELF binary"""
    def __init__(self, target=None, stringio=None):
        """
        target: a binary file or file descriptor
        stringio: an io.BytesIO containing an ELF binary
        """
        self.target = target
        if stringio:
            self.elffile = ELFFile(stringio)
        elif target:
            self.elffile = ELFFile(target)

        self.__setup()

