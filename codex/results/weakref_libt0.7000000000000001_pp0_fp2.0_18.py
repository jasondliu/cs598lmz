import weakref

# Python 3.4 introduced the Enum class
try:
    from enum import Enum
except ImportError:
    Enum = None


class BaseEnum(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        else:
            return self.value == other.value

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return "{} ({})".format(self.name, self.value)

    def __str__(self):
        return self.name


def _make_enum(name, enum_list):
    """
    Creates a class that can be used to represent an enumeration.
    """
    # For Python 3.4 and up, we'll use the Enum class
    if Enum is not None:
        enum_class = Enum(name, enum_list)
        return enum
