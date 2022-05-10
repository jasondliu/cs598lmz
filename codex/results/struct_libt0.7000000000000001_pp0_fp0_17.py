import _struct
import time

from . import _shared

_struct_pack = _struct.pack
_struct_unpack = _struct.unpack
_sys_byteorder = _sys.byteorder

# pylint: disable=too-many-nested-blocks
# pylint: disable=too-many-branches
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-arguments

# This class represents an entire ELF file.
# It contains a number of section and segment
# objects which are used to represent the
# various parts of the ELF file.
class Elf:

    # String to identify little-endian objects:
    ELFCLASS32 = "ELF32"

    # String to identify big-endian objects:
    ELFCLASS64 = "ELF64"

    # Legal values for e_type (object file type).
    ET_NONE = 0         # No file type
    ET_REL = 1          # Relocatable file
    ET_
