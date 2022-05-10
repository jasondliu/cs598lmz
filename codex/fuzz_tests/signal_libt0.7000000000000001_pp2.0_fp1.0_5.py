import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtCore, QtGui

from Orange.data import Table
from Orange.widgets import gui
from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget
from Orange.widgets.utils.itemmodels import DomainModel
from Orange.canvas.report import Report
from Orange.preprocess.preprocess import Preprocess


class OWPasteData(OWWidget):
    name = "Paste Data"
    description = "Construct a data table from a text copied from the clipboard."
    icon = "icons/PasteData.svg"
    priority = 100
    category = "Data"
    keywords = []

    inputs = [("Data", Table, "set_data")]
    outputs = [("Data", Table)]

    want_main_area = False

    autocommit = Setting(True)
    paste_from_file = Setting(True)

    def __init__(self):
        super().__init__()

        self.data
