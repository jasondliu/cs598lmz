import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PySide.QtGui import *
from PySide.QtCore import *

from qt_gui.plugin import Plugin
from python_qt_binding.QtCore import Qt
from python_qt_binding import loadUi

import rospkg
from python_qt_binding.QtGui import QWidget, QFrame, QVBoxLayout
from qt_dotgraph.dot_to_qt import DotToQtGenerator
from qt_dotgraph.dotcode_to_pydot import parse_dotcode
from qt_dotgraph.pydotfactory import PydotFactory
from qt_gui.plugin_context_menu_gfm import PluginContextMenu
from qt_gui.rosimage_picker_gfm import RosImagePicker

class RqtImGuiWidget(QWidget):
	def __init__(self, context, plugin):
		QWidget.__init__(self)
		self.plugin = plugin
		self.context
