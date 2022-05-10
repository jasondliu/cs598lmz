import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont, QTextCharFormat, QColor
import PyQt5.QtCore as QtCore

from pandas_profiling.config import config
from pandas_profiling.report.presentation.core import (
    Field,
    Image,
    Table,
    VariableStats,
    FrequencyTable,
    FrequencyTableSmall,
    Text,
    Widget,
)
from pandas_profiling.utils.paths import get_config_default


class QtPresentation(object):
    """
    Creates a Qt presentation of the dataframe.
    """

    def __init__(self, df, **kwargs):
        # Initialize the application
        self.app = QApplication([])

        # Set the font
        qfont = QFont()
        qfont.setFamily(config["plot"]["font_family"])
        qfont.setPointSize
