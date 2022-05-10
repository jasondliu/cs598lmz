from _struct import Struct
s = Struct.__new__(Struct)
s.size = 1
</code>
this would not eliminate the size check, as it is not exposed anywhere, only added to the init method. as a result, it will still refuse to work with any format other than the predefined ones.
however, the format string is not checked at all before being used. this means we can use our own method to count fields. we need to prepend the format with something to allow a count of the fields, so we can use <code>'/'</code> to start a slice that will slice away a slash and a 2-digit count (or other separator) after the format string. we need to append a custom struct format that will be used only for the calculation and have no real effect on the struct. this will also allow us to handle "new- and old-style formats":
<code>from _struct import Struct
from itertools import count, takewhile

class ExtendedStruct(Struct):
    def __new__(cls, format, endianness="@", prefix="/"):
        size = int("".join(takewhile(str.isdigit, format))) + 1
        if not format.
