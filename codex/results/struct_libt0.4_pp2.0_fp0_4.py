import _struct

#
#-----------------------------------------------------------------------
#

def _get_bit_size(max_value):
    """
    Given a maximum value, return the number of bits needed to represent
    that value.
    """
    return int(math.ceil(math.log(max_value, 2)))

#
#-----------------------------------------------------------------------
#

def _get_bit_mask(bit_size):
    """
    Given a bit size, return a mask that can be used to extract that
    number of bits.
    """
    return (1 << bit_size) - 1

#
#-----------------------------------------------------------------------
#

def _get_bit_mask_for_value(value):
    """
    Given a value, return a mask that can be used to extract the bits
    needed to represent that value.
    """
    return _get_bit_mask(_get_bit_size(value))

#
#-----------------------------------------------------------------------
#

def _get_bit_mask_for_values(values):
    """
    Given a sequence of values, return a mask that can be used to
    extract the
