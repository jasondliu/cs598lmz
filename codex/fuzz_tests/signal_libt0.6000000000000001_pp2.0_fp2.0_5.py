import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Orange.data import Table
from Orange.widgets import gui
from Orange.widgets.settings import Setting
from Orange.widgets.utils.itemmodels import DomainModel
from Orange.widgets.widget import OWWidget
from Orange.widgets.utils.sql import check_sql_input


class OWSave(OWWidget):
    name = "Save"
    description = "Save the data on disk."
    icon = "icons/Save.svg"
    priority = 11

    inputs = [("Data", Table, "set_data")]
    outputs = [("Data", Table)]

    want_main_area = False
    resizing_enabled = False

    auto_apply = Setting(False)
    file_name = Setting("")
    file_format = Setting(0)

    FORMATS = (
        ("Pickled", "pickled"),
        ("Tab-del
