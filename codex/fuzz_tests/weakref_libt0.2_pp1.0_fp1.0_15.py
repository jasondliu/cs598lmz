import weakref

from . import _compat
from . import _util
from . import _weakref
from . import _weakrefset

_logger = logging.getLogger(__name__)


class _DependencyGraph(object):
    """
    A graph of dependencies between objects.

    The graph is represented as a directed acyclic graph (DAG).  Each node in
    the graph represents a single object.  Each edge represents a dependency
    between two objects.  The graph is acyclic because each object can only
    depend on objects that were created before it.

    The graph is used to track dependencies between objects.  When an object
    is garbage collected, it is removed from the graph.  If the object has any
    dependencies, then the objects that depend on it are also removed from the
    graph.  This allows the graph to be used to track dependencies between
    objects that are not directly referenced.

    The graph is also used to track the order in which objects were created.
    When an object is removed from the graph, the objects that depended on it
    are added to a list of objects that
