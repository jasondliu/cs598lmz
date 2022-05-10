import bz2
bz2.__file__

os.__file__

# show path of a module
bz2.__path__


# import as something else, or use from...import...
import bz2 as bz

bz2.BZ2Compressor()

bz.BZ2Compressor()

# import object directly
from os import environ

environ
