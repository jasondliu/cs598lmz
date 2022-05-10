import _struct
struct_unpack = _struct.unpack

from collections import namedtuple

class InvalidMZHeader(Exception):
    pass

PE_TYPE = ['PE32', 'PE32+', 'ROM']

class OptionalHeader(object):
    fmt = '=HHIHHHHHIHHIIQQQ'
    fmt_size = struct_calcsize(fmt)
    fields = ('magic', 'major_linker_version', 'minor_linker_version',
        'size_of_code', 'size_of_initialized_data', 'size_of_uninitialized_data',
        'address_of_entry_point', 'base_of_code', 'base_of_data', 'image_base',
        'section_alignment', 'file_alignment', 'major_operating_system_version',
        'minor_operating_system_version', 'major_image_version', 'minor_image_version',
        'major_subsystem_version', 'minor_subsystem_version', 'win32_version_value',
        'size_
