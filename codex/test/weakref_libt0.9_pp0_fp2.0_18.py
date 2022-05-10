import weakref

from ... import Qt, QtMpl, QtCore
from ...viewer.utils import Timer
from ...common.qt.preferences_dialog import PreferencesDialog
from ...common.qt.mpl_widget import FigWidget
from .utils import _aesthetics, mpl_legend, mpl_title
from .utils import _ImageWindowBase, draggable_legend, _save_dialog, _plot_legend_items

from ...viewer.utils.hooks import connect_callback


class Preferences(object):
    class Plot(object):
        def __init__(self, hidden=[], override={}):
            self.hidden = hidden[:]
            self.override = dict(override)


