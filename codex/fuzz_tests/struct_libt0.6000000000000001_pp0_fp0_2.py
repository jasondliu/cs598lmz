import _struct

from .utils import bytes_to_int, int_to_bytes, int_to_bit_array, bit_array_to_int


def _get_struct_format(bit_length):
    """Get the struct format for a given bit length.

    Args:
        bit_length (int): The bit length.

    Returns:
        str: The struct format.

    """
    if bit_length < 8:
        raise ValueError("Bit length must be at least 8")

    if bit_length % 8 != 0:
        raise ValueError("Bit length must be a multiple of 8")

    return '!{}B'.format(bit_length // 8)


def _get_bit_array_length(bit_length):
    """Get the length of a bit array for a given bit length.

    Args:
        bit_length (int): The bit length.

    Returns:
        int: The bit length of the bit array.

    """
    return bit_length + 1


def _get_bit_array_format(bit_length):
    """Get the
