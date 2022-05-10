import gc, weakref

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Holder(Widget):
    """A place to hold other Widgets.

    This is a place to put Widgets that aren't parented by any other Widget.
    """

    #: The Widget that is being held.
    widget = ObjectProperty(None, rebind=True)

    def add_widget(self, widget):
        if self.widget:
            raise Exception('Holder can only hold one Widget')
        self.widget = widget
        widget.parent = self # HACK!

    def remove_widget(self, widget):
        if widget is self.widget:
            self.widget = None
        else:
            raise Exception('not my widget')
        widget.parent = None # HACK!


"""
TODO: It would be nice if we could make this work like

with WidgetHolder() as widget:
    do_stuff_with_widget(widget)

i.e., it sets up and tears down the widget automatically.
"""



