import _struct
from _struct import *

from ctypes import *
from ctypes.wintypes import *

from . import *

#------------------------------------------------------------------------------

class PE_FILE_HEADER(Structure):
    _pack_ = 1
    _fields_ = [
        ("Machine",                 WORD),
        ("NumberOfSections",        WORD),
        ("TimeDateStamp",           DWORD),
        ("PointerToSymbolTable",    DWORD),
        ("NumberOfSymbols",         DWORD),
        ("SizeOfOptionalHeader",    WORD),
        ("Characteristics",         WORD),
    ]

class PE_OPTIONAL_HEADER(Structure):
    _pack_ = 1
    _fields_ = [
        ("Magic",                   WORD),
        ("MajorLinkerVersion",      BYTE),
        ("MinorLinkerVersion",      BYTE),
        ("SizeOfCode",              DWORD),
        ("SizeOfInitializedData",   DWORD),
        ("SizeOfUninitializedData", DWORD),
        ("AddressOfEntryPoint",     DWORD
