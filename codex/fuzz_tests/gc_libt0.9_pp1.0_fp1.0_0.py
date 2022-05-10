import gc, weakref
from pyqtgraph.Qt import QtGui, QtCore

"""
This module provides functions for automatically building a GUI from a data tree.
See ParameterTree.build() for details.
"""


def _parameterItemFromItem(item, root):
    """Return the ParameterItem which owns this QTreeWidgetItem"""
    while item is not None and item is not root:
        if item in item.treeWidget().items:
            return item.treeWidget().items[item]
        item = item.parent()


class Parameter(AbstractParameter):
    sigTreeStateChanged = QtCore.Signal(object)
    sigStateChanged = QtCore.Signal(object)
    sigValueChanged = QtCore.Signal(object, object)
    sigChildAdded = QtCore.Signal(object, object)
    sigChildRemoved = QtCore.Signal(object, object)

    def __init__(self, **opts):
        """
        opts holds a number of options that are used to configure the parameter.  
           name=string            Fixed name of this parameter. Default
