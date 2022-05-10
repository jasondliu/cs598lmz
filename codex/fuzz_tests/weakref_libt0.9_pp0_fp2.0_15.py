import weakref
from collections import OrderedDict
import logging
log = logging.getLogger(__name__)


class Widget(object):
    """ Parent class for all widgets, does not represent the Tree itself.
    """
    __slots__ = ['parent']

    def __init__(self, parent):
        self.parent = weakref.ref(parent)

    def _parent(self):
        return self.parent()

    def on_enable(self):
        """ Called when the widget is made visible.
        """
        pass

    def on_disable(self):
        """ Called when the widget is made invisible.
        """
        pass

    def on_select(self):
        """ Called when the widget is selected.
        """
        pass


class WidgetManager(Widget):
    """ Parent class for all entities that contain and manage other widgets.
    """
    __slots__ = ['widgets', 'ui_manager']

    def __init__(self, parent):
        Widget.__init__(self, parent)
        self.widgets = OrderedDict
