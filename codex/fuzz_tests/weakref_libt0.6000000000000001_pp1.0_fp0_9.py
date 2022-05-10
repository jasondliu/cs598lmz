import weakref

from cogent3.core.alignment import SequenceCollection
from cogent3.core.tree import PhyloNode
from cogent3.parse.tree import DndParser
from cogent3.util.dict_array import DictArrayTemplate, DictArray


__author__ = "Gavin Huttley"
__copyright__ = "Copyright 2007-2020, The Cogent Project"
__credits__ = ["Gavin Huttley"]
__license__ = "BSD-3"
__version__ = "2020.2.7a"
__maintainer__ = "Gavin Huttley"
__email__ = "gavin.huttley@anu.edu.au"
__status__ = "Alpha"


_default_tree_factory = DndParser


class TreeError(Exception):
    pass


class TreeNode(PhyloNode):
    """A TreeNode is a Tree that has a parent.

    It also has a branch length and branch support.
    """

    def __init__(self, Name, Length=None, Support=None, **kw):
