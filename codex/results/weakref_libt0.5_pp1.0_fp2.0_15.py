import weakref

from . import node
from . import utils
from . import command
from . import event
from . import error
from . import config
from . import logger

log = logger.getChild(__name__.split('.')[-1])


class Node(node.Node):
    """
    A node in the data tree.
    """

    #: Node type name.
    type_name = 'node'

    #: Node type icon.
    type_icon = 'node'

    #: Node type description.
    type_description = 'Node'

    #: List of node type names that can be children of this node.
    child_type_names = []

    #: List of node type names that can be parents of this node.
    parent_type_names = []

    #: List of node type names this node can be copied into.
    copy_type_names = []

    #: List of node type names this node can be moved into.
    move_type_names = []

    #: List of node type names this node can be linked into.
    link_type
