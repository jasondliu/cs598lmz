import _struct

# pylint: disable=unused-import
from typing import Any, Dict, List, Optional, Tuple, Type, Union
from mypy_extensions import TypedDict

# pylint: enable=unused-import


def _make_struct(fmt: str) -> _struct.Struct:
    """Create a struct type using the given format string."""
    return _struct.Struct(fmt)


# The following constants are used to represent the type of a message.
#
# The first byte of a message is the message type. It can be one of the
# following values.
#
# The value 0 is not used.
#
# The value 1 is used for a message containing a string.
#
# The value 2 is used for a message containing a number.
#
# The value 3 is used for a message containing a string and a number.
#
# The value 4 is used for a message containing a string and a list of
# numbers.
#
# The value 5 is used for a message containing a string and a dictionary
# of numbers.
#
#
