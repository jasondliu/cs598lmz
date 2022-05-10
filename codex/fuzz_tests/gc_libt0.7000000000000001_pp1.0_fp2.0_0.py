import gc, weakref
from itertools import izip

from twisted.python import log
from twisted.internet import defer, threads

from . import crypto, errors, schema
from .util import assert_type, BufferTooShort, get_options
from .cassandra.ttypes import ConsistencyLevel, ColumnPath, ColumnParent, Column
from .cassandra.cassandra import Cassandra

from .marshal import int32_pack, int32_unpack
from .marshal import write_longstring, read_longstring
from .marshal import write_stringlist, read_stringlist
from .marshal import write_consistencylevel, read_consistencylevel
from .marshal import write_columnpath, read_columnpath
from .marshal import write_columnparent, read_columnparent
from .marshal import write_column, read_column
from .marshal import write_bytebuffer, read_bytebuffer

schema.validate_class(Column, 'Column')
schema.validate_class(ColumnPath, 'ColumnPath')
schema.validate
