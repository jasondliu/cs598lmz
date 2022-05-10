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
_immutable_objects = [
    _objects.NameObject('null'),
    _objects.NameObject('true'),
    _objects.NameObject('false'),
    _objects.NameObject('R'),
    _objects.NameObject('stream'),
    _objects.NameObject('endstream'),
    _objects.NameObject('obj'),
    _objects.NameObject('endobj'),
    _objects.NameObject('xref'),
    _objects.NameObject('trailer'),
    _objects.NameObject('startxref'),
    _objects.NameObject('f
