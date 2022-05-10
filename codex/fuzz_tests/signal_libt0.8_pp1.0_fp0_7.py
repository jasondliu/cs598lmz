import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

from orangewidget import gui as OWWidgetGui
from orangewidget.settings import Setting
from orangewidget import widget as OWWidget
from orangewidget.gui import OWGUI
from Orange.data.sql.table import SqlTable, LARGE_TABLE

from .. import widgets
from ..widgets.gui import SelectRowsColumnsDomain
from ..widgets.gui import SELECTCOLUMNS_BASE, SELECTROWS_BASE
from ..widgets.gui import SELECTROWS_RANGE, SELECTROWS_WHERE
from ..widgets.gui import SELECTROWS_ORDERBY, SELECTROWS_LIMIT
from ..widgets.gui import SELECTCOLUMNS_NAMES, SELECTCOLUMNS_TYPES
from ..widgets.gui import SETTINGS_DOMAIN


class OWSqlTable(OWWidget.OWWidget):
    settingsList = [

