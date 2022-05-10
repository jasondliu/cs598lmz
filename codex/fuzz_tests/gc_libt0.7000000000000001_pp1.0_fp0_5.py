import gc, weakref
import logging
logger = logging.getLogger(__name__)

from . import slots

class Widget(QWidget, slots.Slots):
    """
    Base class for all widgets.
    """
    def __init__(self, name=None, parent=None):
        """
        :param name: a name to be used as the widget's objectName
        :param QWidget parent: the parent widget

        All widgets are created with a parent widget (even the main window is
        a widget). The widgets are deleted when the parent is deleted.

        A widget can be created at the class level (i.e. a class attribute),
        in which case its parent is set to the class's `.parent` attribute,
        which should be a QWidget.
        """
        super().__init__(parent or self.parent)
        if name:
            self.setObjectName(name)
        if parent:
            parent.addChild(self)
        else:
            self.setParent(self.parent)
        self.setFocusPolicy(Qt.StrongFocus)
       
