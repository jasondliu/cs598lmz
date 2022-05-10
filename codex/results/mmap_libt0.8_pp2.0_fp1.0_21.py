import mmap
import shutil
import tempfile
import pytest

from elftools.elf.elffile import ELFFile
from elftools.elf.elffile import ELFError
from elftools.elf.elffile import ELFRelocationSection
from elftools.elf.sections import SymbolTableSection
from elftools.elf.sections import NoteSection
from elftools.elf.descriptions import describe_p_type
from elftools.elf.constants import P_TYPE
from elftools.elf.dynamic import DynamicTag
from elftools.elf.dynamic import DynamicSection
from elftools.elf.gnuversions import (
    GnuVerNeedSection, GnuVerDefSection, GnuVerDefEntry,
    GnuVerSymSection, GnuVerSym)
from elftools.elf.gnuverneed import GnuVerNeedSection
from elftools.common.exceptions import ELFError
from elftools.common.py3compat import bytes2str
from elftools.common.py3compat import itervalues


# =================
