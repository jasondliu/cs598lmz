import weakref

from pyjamas.rpc import JSONParser
from pyjamas.rpc.ServiceProxy import ServiceProxy
from pyjamas import Window
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.HasAlignment import HasAlignment
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.Button import Button
from pyjamas.ui.ScrollPanel import ScrollPanel
from pyjamas.ui.Tree import Tree, TreeItem, TreeListener
from pyjamas.ui.CheckBox import CheckBox
from pyjamas.ui import HasHorizontalAlignment as HHorz
from pyjamas.ui import HasVerticalAlignment as HVert
from pyjamas import HasAlignment as BaseAlignment
from HDict import HDict



# TODO: For consistency, the tree-handling routines should all have
# a prefix of tree_: I don't think TreeItem instance methods are
# intended to be called from outside the class
