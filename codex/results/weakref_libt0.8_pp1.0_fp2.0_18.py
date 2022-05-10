import weakref
import webbrowser
import urllib

from PyQt5 import QtCore, QtGui, QtWidgets

from . import *
from . import icons, view
from . import model as model_module
from . import widgets
from . import utils

class BasePlugin:
    """
    Base class for plugins.

    Plugins derive from this class and override the methods they need.
    The plugin is itself a QDockWidget and contains a QWidget.
    The QWidget is the one displayed by the QDockWidget, but it is
    not replaced.

    The :meth:`create_widget` method must be implemented. It creates
    the widget that will be displayed in the dock.

    The :meth:`get_menu_actions` can be overridden to provide a list
    of actions that will be added to the context menu of the dock
    title bar.

    The :meth:`get_title_buttons` can be overridden to provide a list
    of widgets that will be displayed on the title bar of the dock.

    The :meth:`get_
