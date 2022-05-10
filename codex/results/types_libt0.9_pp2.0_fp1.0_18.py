import types
types.MethodType(lambda self: "", "", "")

import elftools
from elftools.elf import elffile
from elftools.elf.enums import ENUM_P_TYPE
from elftools.elf.sections import SymbolTableSection
from elftools.elf.relocation import RelocationSection
from elftools.elf.descriptions import describe_gnu_reloc_type
from elftools.dwarf.descriptions import describe_form_class
from elftools.common.py3compat import bytes2str

from hashlib import sha1
from binascii import b2a_hex

from capstone import Cs, CS_ARCH_X86, CS_MODE_32
from capstone import CS_MODE_64
from capstone import CS_ARCH_ARM, CS_ARCH_ARM64, CS_ARCH_MIPS
from keystone import Ks, KS_ARCH_ARM, KS_MODE_ARM, KS_MODE_THUMB, KS_MODE_THUMBBE
from keystone import KS_ARCH_ARM64, KS_MODE
