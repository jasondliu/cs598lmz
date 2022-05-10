import _struct

from ._compat import PY3


def pack(fmt, *args):
    """
    Pack the given arguments according to the format string fmt.
    The return value is a bytes object.

    :param fmt: format string
    :param args: arguments
    :return: packed object
    """
    return _struct.pack(fmt, *args)


def pack_into(fmt, buffer, offset, *args):
    """
    Pack the given arguments according to the format string fmt.
    The return value is a bytes object.

    :param fmt: format string
    :param buffer: buffer to write to
    :param offset: offset in buffer
    :param args: arguments
    :return: packed object
    """
    return _struct.pack_into(fmt, buffer, offset, *args)


