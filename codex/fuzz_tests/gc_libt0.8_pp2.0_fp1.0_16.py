import gc, weakref
import warnings
import numpy as np

from AnyQt.QtCore import Qt, QUrl, QObject, QEvent, QEventLoop
from AnyQt.QtWidgets import QAction
from AnyQt.QtGui import QDesktopServices
import pyqtgraph as pg

from Orange.data import Table, Domain, ContinuousVariable
from Orange.widgets.utils.state_summary import format_summary_details
from Orange.widgets import gui, settings
from Orange.widgets.utils.annotated_data import (create_annotated_table,
                                                 ANNOTATED_DATA_SIGNAL_NAME)
from Orange.widgets.utils.concurrent import (
    TaskState, ConcurrentWidgetMixin, ThreadExecutor,
    job_state_async_slot, remove_jobs_before,
    task_finished_string)

from orangecontrib.network.network.base.network import Network, BaseEdge
from orangecontrib.network.network.base.load import (BaseNetworkLoader,
                                                     NetworkLoadError)
from orangecontrib.network.
