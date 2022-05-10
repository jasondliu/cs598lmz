import mmap
# Test mmap.mmap()
mmap.mmap(-1, 1).read_byte()

# no mmap.mmap() is availabe in jython
if sys.platform == "java":
    from test import test_mmap as testmod
else:
    from test import test_mmap_extra as testmod

# Brief digression to test import hooks...
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "loader"))
from . import simpleloader
from . import badsyntax_exc
from . import badsyntax_exc3
from . import badsyntax_future3
from . import packagedloader
from . import badpackage
from . import my_namespace_pkg
from . import w_long
from . import w_long_future
from . import w_future3
from . import bad_future3_encoding
from . import bad_source_encoding
from . import sysloader
from . import my_namespace_pkg.sub
from . import x_level
from . import x_level2
from . import x_level2
from
