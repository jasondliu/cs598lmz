import _struct as struct

from . import _parsers, _utils

if sys.version_info[0] == 2:
    def long(x):
        return int(x)


class _Error(Exception):
    pass


class _NotImplementedError(_Error):
    pass


class _InvalidFormatError(_Error):
    pass


class _InvalidDataError(_Error):
    pass


class _UnknownFormatError(_Error):
    pass


class _UnknownSubFormatError(_Error):
    pass


class _UnknownTypeError(_Error):
    pass


class _UnknownConstantError(_Error):
    pass


class _UnknownEndianError(_Error):
    pass


class _UnknownFieldTypeError(_Error):
    pass


class _UnknownFieldError(_Error):
    pass


class _FieldDefinitionError(_Error):
    pass


class _ArrayItemError(_Error):
    pass


class _FieldType(_utils.Enum):
    INTEGER = 1
    FLOAT = 2
    STRING = 3
    BINARY_DATA =
