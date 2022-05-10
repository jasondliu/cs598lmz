from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hhl', byteorder='big')
s.pack(1, 2, 3)

# _struct.__doc__

from _struct import __doc__
print(__doc__)

# _struct.__file__
from _struct import __file__
print(__file__)

# _struct.__name__

from _struct import __name__
print(__name__)

# _struct.__package__
from _struct import __package__
print(__package__)

# _struct.__version__
from _struct import __version__
print(__version__)

# _struct.calcsize
from _struct import calcsize
calcsize('hhl')

# _struct.pack
from _struct import pack
pack('hhl', 1, 2, 3)

# _struct.pack_into
from _struct import pack_into
s = bytearray(12)
pack_into('hhl', s, 0, 1, 2, 3)
s

# _struct.unpack
