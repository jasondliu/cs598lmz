import weakref

import numpy as np

from Orange.data import \
    ContinuousVariable, DiscreteVariable, StringVariable, TimeVariable, \
    Domain, Table, Storage, Variable
from Orange.data.util import get_unique_names, get_unique_names_duplicates
from Orange.util import Reprable, ReprableList, color_to_hex
from Orange.widgets import gui, settings
from Orange.widgets.utils.annotated_data import create_annotated_table
from Orange.widgets.utils.colorpalettes import DefaultRGBColors
from Orange.widgets.utils.concurrent import TaskState, ConcurrentWidgetMixin
from Orange.widgets.utils.itemmodels import PyTableModel
from Orange.widgets.utils.sql import check_sql_input
from Orange.widgets.widget import OWWidget, Msg, Input, Output


class _VariableListModel(PyTableModel):
    """Variable list model.

    Parameters
    ----------
    variables : list of Variable
        Variables to be displayed in the list.
    parent : QObject
        Parent Q
