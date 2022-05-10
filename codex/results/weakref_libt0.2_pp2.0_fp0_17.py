import weakref

from . import _base
from . import _compat
from . import _util
from . import _types
from . import _errors
from . import _protocol


class _Cursor(_base.Cursor):
    """Cursor object for accessing the results of a query.

    The Cursor class represents a cursor to iterate over Mongo query results.
    """

    def __init__(self, collection, spec, fields, skip, limit,
                 timeout, snapshot, tailable, sort, max_scan,
                 as_class, slave_okay, await_data, partial, manipulate,
                 read_preference, tag_sets, secondary_acceptable_latency_ms,
                 _must_use_master, _is_command, _uuid_subtype,
                 _read_concern, _session, _client, _codec_options,
                 _compile_re, _event_listeners):
        """Create a new cursor.

        Should not be called directly by application developers - see
        :meth:`~pymongo.collection.Collection.find` instead.

       
