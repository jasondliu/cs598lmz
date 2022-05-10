import gc, weakref, inspect
import os
import logging
import re

class WidgetTracker:
    def __init__(self):
        """Initialize the widget tracker.
        
        Initialize the widget tracker and create the weakref to the bound widgets.
        The widgets are tracked by type and name."""
        self.widgets = {}
        self.widgets["name"] = weakref.WeakValueDictionary()
        self.widgets["type"] = weakref.WeakValueDictionary()
        
    def register_widget(self, widget):
        """Registers a widget with the WidgetTracker.
        
        Only widgets that are not None and that do not have None as a name
        are registered."""
        if widget != None and widget.name != None:
            if self.widgets["name"].has_key(widget.name):
                logging.warning("Widget %s got registered twice. Replacing previous widget." % self.widgets["name"][widget.name])
            self.widgets["name"][widget.name] = widget
            self.widgets["type"][widget.__class
