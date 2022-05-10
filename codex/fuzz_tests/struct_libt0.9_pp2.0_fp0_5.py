import _struct
import calendar
import time
from elftools.elf.elffile import ELFFile, SymbolTableSection
from elftools.elf.dynamic import DynamicSection
from elftools.elf.enums import ENUM_D_TAG

class Image:
    # Structure describing a memory area.
    MemArea = namedtuple('MemArea', 'addr size name')

    # Symbol table entry.
    Symbol = namedtuple('Symbol', 'name addr addend')

    # Constructor.
    def __init__(self, fp, name = None):
        self.fp = fp
        self.name = name

    # open() method.
    def open(self):
        size = os.fstat(self.fp.fileno()).st_size
        return self._open(self.fp.read(size))

    # open_memory() method.
    def open_memory(self, addr, data):
        return self._open(data, addr)

    # _open() method.
    def _open(self, data, addr = 0):
        self.
