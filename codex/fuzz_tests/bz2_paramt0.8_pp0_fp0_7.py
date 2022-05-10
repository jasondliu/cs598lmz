from bz2 import BZ2Decompressor
BZ2Decompressor

from util import *
from varint import *
from section import *
from datatypes import *
from expression import *
from instructions import *
from module import *

class ModuleReader(object):
    def __init__(self, f):
        self.f = f
        self.compressed = False

        self.base_offset = 0
        self.version = None
        self.sources = []
        self.functions = []
        self.data = []
        self.start_function = None
        self.exports = []
        self.imports = []

        self.__read_header()
        self.__read_sections()

    def __read_header(self):
        sig = self.f.read(4)
        if sig == b"\0asm":
            self.base_offset = 4
        elif sig == b"\0\0asm":
            self.base_offset = 8

    def __read_sections(self):
        while True:
            section_id, data = read_section(self.f)
            if section_
