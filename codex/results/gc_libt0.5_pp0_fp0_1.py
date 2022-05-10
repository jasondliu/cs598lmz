import gc, weakref
import sys

from . import _graph
from . import _node
from . import _transform

def _get_node_id(node):
    return id(node)

def _get_node_name(node):
    return node.name

def _get_node_label(node):
    return node.label

def _get_node_attrs(node):
    return node.attrs

def _get_node_node_attrs(node):
    return node.node_attrs

def _get_node_edge_attrs(node):
    return node.edge_attrs

def _get_node_children(node):
    return node.children

def _get_node_parents(node):
    return node.parents

def _get_node_siblings(node):
    return node.siblings

def _get_node_descendants(node):
    return node.descendants

def _get_node_ancestors(node):
    return node.ancestors

def _get_node_root(node):
