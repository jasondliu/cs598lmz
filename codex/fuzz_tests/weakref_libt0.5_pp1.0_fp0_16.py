import weakref

from . import _lib
from . import _util
from . import _types
from . import _errors

from . import _lib
from . import _util
from . import _types
from . import _errors


class _Base(object):
    """
    Base class for all objects in the Neo4j API.

    This class provides a common base for all Neo4j API objects.
    It is not meant to be used directly.

    :ivar _handle: The native Neo4j handle for this object.
    :vartype _handle: int
    :ivar _graph: The graph to which this object belongs.
    :vartype _graph: Graph
    """

    def __init__(self, handle, graph):
        """
        Initialize a new Neo4j object.

        :param handle: The native Neo4j handle for this object.
        :type handle: int
        :param graph: The graph to which this object belongs.
        :type graph: Graph
        """
        self._handle = handle
        self._graph = weakref.ref(graph)

   
