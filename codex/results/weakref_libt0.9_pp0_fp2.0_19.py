import weakref
import gst
import gobject

LOGGER = logging.getLogger('autonetkit.gst')


# TODO: move drawing to layout

class GstNetwork(object):
    "Network container for GstNodes"

    def __init__(self):
        self.nodes = {}  # indexed by name

    def node(self, name=None):
        """Returns the node with name
        create it if it does not exist"""
        if name not in self.nodes:
            self.nodes[name] = GstNode(name)
        # Note the use of weakref and the id() so don't need to keep track of which
        # nodes are still in use
        return self.nodes[name]


class GstNode(object):
    """GstNetwork node"""

    def __init__(self, name=None):
        self.pipelines = {}
        self.name = name
        self.scale = 1
        self.x = None
        self.y = None
        self.scale = 1
        self.anchor =
