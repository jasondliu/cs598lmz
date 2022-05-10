import weakref

from . import base
from . import models
from . import exceptions
from . import util
from . import signals
from . import query
from . import query_compiler
from . import query_context
from . import query_result
from . import options


class ModelNotFound(Exception):
    pass


class Session(base.Object):
    """
    The session object is used to store, retrieve and delete
    objects to and from the database.

    It also provides a method for flushing pending changes to the
    database, and for rolling back the transaction.

    A session object is instantiated using the ``session()`` method
    from a :class:`Model` class.
    """

    _autoflush = True
    _autocommit = True
    _autorollback = True

    #: Indicates whether the session has been closed.
    closed = False

    #: A weakref to the :class:`Model` class that created this
    #: session.
    model = None

    #: The options used to create this session.
    options = None

