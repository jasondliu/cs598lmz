import weakref

from . import _py3k as _3k
from . import _py2 as _2

_3k.NotImplemented = _2.NotImplemented
_3k.NotImplementedError = _2.NotImplementedError
_3k.long = _2.long
_3k.unicode = _2.unicode
_3k.basestring = _2.basestring
_3k.imap = _2.imap
_3k.izip = _2.izip
_3k.xrange = _2.xrange
_3k.intern = intern
_3k.range = range
_3k.zip = zip
_3k.map = map
_3k.maxint = _2.maxint
_3k.raw_input = _2.raw_input
_3k.reduce = reduce
_3k.iteritems = _2.iteritems
_3k.iterkeys = _2.iterkeys
_3k.itervalues = _2.itervalues
_3k.
