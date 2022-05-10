import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from AnyQt.QtCore import pyqtSlot as Slot
from Orange.data import Table, Variable, ContinuousVariable, DiscreteVariable
from Orange.widgets import widget, gui, settings
from Orange.widgets.utils.annotated_data import (create_annotated_table,
                                                 ANNOTATED_DATA_SIGNAL_NAME)
from Orange.widgets.utils.colorpalettes import CustomColorPalette
from Orange.widgets.widget import Input, Output


class OWDistribution(widget.OWWidget):
    name = "Distributions"
    description = "View the distribution of a variable's values."
    priority = 110
    icon = "icons/Distribution.svg"
    keywords = ["histogram"]

    Inputs = [("Data", Table, "set_data"),
              ("Features", Table,
               "set_features"),
              ("Data Subset", Table,
               "set_data_subset")]

    Outputs = [("Selected Data", Table),
              
