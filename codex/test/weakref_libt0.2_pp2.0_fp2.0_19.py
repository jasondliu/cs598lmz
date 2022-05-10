import weakref

from . import _util
from . import _py3compat
from . import _compat
from . import _compression
from . import _constants
from . import _errors
from . import _filters
from . import _objects
from . import _parser
from . import _qpdf
from . import _streams
from . import _xref

# This is a list of all the objects that are not allowed to be
# modified.  This list is used to check for modifications to
# objects that are not allowed.
