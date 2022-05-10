import weakref

from rpython.rlib import rawrefcount, rgc
from rpython.rlib.rarithmetic import r_uint, highest_bit


def _compute_bits_for_one_page(alignment):
    """compute the number of bits necessary to encode an address
    in one page.  For example, if an address is aligned in 8 bytes,
    there are 3 bits necessary, so objects are aligned in 8*(2^3) = 64 bytes
    """
    return highest_bit(alignment)

class AddressDict(object):
    """Dictionary mapping address to object.  The object can be finalized
    by calling remove(address).
    """
    _immutable_ = True

    def __init__(self, alignment=rawrefcount.ALIGNMENT):
        self.alignment = alignment
        self.bits_for_one_page = _compute_bits_for_one_page(alignment)
        self.objects_with_finalizer = {}
        self.addresses_with_finalizer = {}
        self.number_of_objects = 0

