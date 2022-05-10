import _struct

from .compat import PY3, xrange

if PY3:
    long = int

__all__ = ["pack", "unpack", "calcsize", "pack_into", "unpack_from"]

def _compute_size(fmt, *args):
    size = 0
    for option in fmt:
        if option == "x":
            size += 1
        elif option in "bB":
            size += 1
        elif option in "hH":
            size += 2
        elif option in "iIlL":
            size += 4
        elif option in "qQ":
            size += 8
        elif option in "nN":
            size += 2
        elif option in "f":
            size += 4
        elif option in "d":
            size += 8
        elif option == "s":
            size += args[0]
            args = args[1:]
        elif option == "p":
            size += args[0]
