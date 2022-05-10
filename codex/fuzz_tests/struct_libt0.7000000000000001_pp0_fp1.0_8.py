import _struct
from typing import Optional, Sequence, Union

__all__ = ["format_size", "memoryview_contiguous", "memoryview_is_contiguous"]

_nbytes_per_type = _struct.calcsize("@P")


def format_size(nbytes: int) -> str:
    """Format a number of bytes as a human-readable size.  The result is
    similar to the "h" option in the GNU ls(1) utility (e.g., "1.2M").

    Parameters
    ----------
    nbytes : int
        Number of bytes to format

    Returns
    -------
    str
        Human-readable size

    Examples
    --------
    >>> format_size(2 ** 20)
    '1.0M'
    """
    power = int(math.log2(nbytes) / 10)
    if power >= len(_binary_prefixes):
        power = len(_binary_prefixes) - 1
    return f"{nbytes / (2 ** (10 * power)):.1f}{_binary_prefixes[power]}"


