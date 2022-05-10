import gc, weakref
from functools import partial

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Orange.data import Table, Domain, ContinuousVariable, DiscreteVariable
from Orange.widgets import gui, settings
from Orange.widgets.utils.itemmodels import DomainModel
from Orange.widgets.utils.sql import check_sql_input
from Orange.widgets.widget import OWWidget, Input, Output
from Orange.widgets.utils.widgetpreview import WidgetPreview
from Orange.widgets.utils.state_summary import format_summary_details
from Orange.widgets.utils.concurrent import TaskState, ConcurrentWidgetMixin

from orangecontrib.datafusion.models import Relation, RelationCompleter
from orangecontrib.datafusion.widgets.owfusedata import FuseData
from orangecontrib.datafusion.widgets.owfusedata import (
    RelationCompleterTask, RelationCompleterTaskState)
from orangecontrib.datafusion.widgets.owfusedata
