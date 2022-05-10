import lzma
# Test LZMADecompressor
CLASS_TO_TYPE = {
    'b': (1, "<"),
    'B': (1, "<"),
    'H': (2, "<"),
    'I': (4, "<"),
    'Q': (8, "<"),
    'f': (4, "<"),
    'd': (8, "<"),
    'P': (1, "<"),
    'x': (1, "<"),
    'c': (1, "<"),
}


class HeaderField(object):
    """
    Represents a variable in the header.
    """

    def __init__(self, fmt, name, callback=None):
        if not set(fmt) <= set("bBHIfdPxc"):
            raise Exception("Illegal fmt string: " + fmt)
        self.fmt = fmt
        self.name = name
        self.callback = callback
        self.__doc__ = self.callback.__doc__

    def decode(self, s):
        """
        :type s: bytes
        """
        r = collections.namedtuple("_
