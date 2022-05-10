import mmap
# Test mmap.mmap(0, 1, 'ij', mmap.ACCESS_WRITE)


PY3 = sys.version_info[0] == 3

if PY3:
    def b(x):
        return x.encode('latin-1')

    def u(x):
        return x

    bytes = bytes
else:
    def b(x):
        return x

    def u(x):
        return unicode(x, "unicode_escape")

    bytes = str


class PrettyPrinter:

    def __init__(self, *, indent="    ", bold=True, width=4, compact=False):
        #: Indentation for this printer.  Can be changed at any time.
        #: Print will only add continuation lines if the current line
        #: has at least this many characters.
        self._indent = indent
        self._bold = bold
        self._width = width
        self._compact = compact
        self._out = bytearray()
        self._new_line_indent = ""

    @property
    def indent
