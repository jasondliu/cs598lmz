import gc, weakref

from .. import utils
from .. import errors
from .. import layouts
from .. import extra


__all__ = ['Layout', 'LayoutTemplates', 'LayoutNode', 'LayoutNodeTemplate', 'LayoutConnection', 'LayoutConnectionTemplate']


class Layout(object):
    '''
    Base class for all layouts.
    '''
    
    def __init__(self, nodes, connections):
        '''
        Initialize a layout.
        
        :param nodes: Node information.
        :type nodes: list of dicts or a dict.
        :param connections: Connection information.
        :type connections: list of dicts.
        '''
        self._nodes = nodes
        self._connections = connections
        
        self._node_cache = {}
        self._node_templates = None
        self._connection_templates = None
    
    @property
    def nodes(self):
        '''
        Get the nodes in the layout.
        
        :return: A list of node templates.
        :rtype: list
        '''
        if self._node
