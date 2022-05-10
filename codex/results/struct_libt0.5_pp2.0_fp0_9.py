import _struct

from . import _structutils
from . import _utils


class _StructMeta(type):
    """
    A metaclass for all structs.
    """

    def __new__(mcs, name, bases, dct):
        # Make sure that the fields are in the correct format.
        dct['_fields'] = _utils.normalize_fields(dct['_fields'])

        # Set the __slots__ to the fields.
        dct['__slots__'] = tuple(dct['_fields'].keys())

        # Create the struct.
        struct = super().__new__(mcs, name, bases, dct)

        # Create the struct format.
        struct._struct_format = _structutils.create_struct_format(struct._fields)

        # Create the struct packer.
        struct._struct_packer = _struct.Struct(struct._struct_format)

        # Create the struct unpacker.
        struct._struct_unpacker = _struct.Struct(struct._struct_format)

        return struct


class Struct
