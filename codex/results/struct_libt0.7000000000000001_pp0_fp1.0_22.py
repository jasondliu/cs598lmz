import _struct

# This is our implementation of the struct module.
# It's very limited and only supports values that we need for DWARF encoding.
# TODO(dberris): Extend this for more types.
_struct.unpack = _dwarf_unpack
_struct.pack = _dwarf_pack
_struct.calcsize = _dwarf_calcsize

# DWARF constants.
DW_ATE_address = 0x01
DW_ATE_boolean = 0x02
DW_ATE_complex_float = 0x03
DW_ATE_float = 0x04
DW_ATE_signed = 0x05
DW_ATE_signed_char = 0x06
DW_ATE_unsigned = 0x07
DW_ATE_unsigned_char = 0x08
DW_ATE_imaginary_float = 0x09
DW_ATE_packed_decimal = 0x0a
DW_ATE_numeric_string = 0x0b
DW_ATE_edited = 0x0c
DW_ATE_signed_fixed = 0x0d
DW_ATE_unsigned_
