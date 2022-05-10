import weakref
from collections import defaultdict

from PyQt5.QtCore import pyqtSignal, QObject, QTimer
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QMouseEvent, QWheelEvent, QKeyEvent
from PyQt5.QtCore import Qt

from . import mpl_canvas
from . import mpl_widget
from . import mpl_toolbar
from . import mpl_toolbar_widget

from . import mpl_navigation_toolbar
from . import mpl_navigation_toolbar_widget
from . import mpl_navigation_toolbar2
from . import mpl_navigation_toolbar2_widget
from . import mpl_navigation_toolbar3
from . import mpl_navigation_toolbar3_widget

from . import mpl_figure_manager
from . import mpl_figure_manager_widget

from . import mpl_backend_qt5agg
from . import mpl_backend_qt5
from . import mpl_
