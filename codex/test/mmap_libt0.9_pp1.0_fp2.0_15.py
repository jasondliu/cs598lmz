import mmap
import tempfile
import traceback

from .core import get_mnemonics, get_nodes
from . import utils

class Node(object):
    def __init__(self, name, offset, number, type, src, value=None, children=None):
        self.name = name
        self.number = number
        self.offset = offset
        self.type = type
        self.src = src
        self.value = value
        if children == None:
            self.children = []
        else:
            self.children = children
        self.detail = []

class CodeAnalyzer(object):
    def __init__(self, binfile, outputfile, verbose=0):
        bindata, start_offset, end_offset, cmd_section_offset, reloc_section_offset, string_data = utils.read_code_section(binfile)
        self.start_offset = start_offset
        self.end_offset = end_offset
        self.cmd_section_offset = cmd_section_offset
        self.reloc_section_
