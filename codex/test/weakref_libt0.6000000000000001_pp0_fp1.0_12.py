import weakref

import numpy as np
import pandas as pd
from scipy.sparse import issparse, csr_matrix
from scipy.spatial.distance import cdist

from Orange.data import Table
from Orange.preprocess.transformation import Identity
from Orange.projection import SklProjector, Projection
from Orange.util import deprecated_members
from Orange.widgets import widget, gui
from Orange.widgets.settings import Setting
from Orange.widgets.utils.annotated_data import (create_annotated_table,
                                                 ANNOTATED_DATA_SIGNAL_NAME)
from Orange.widgets.utils.concurrent import TaskState, ConcurrentWidgetMixin
from Orange.widgets.utils.itemmodels import DomainModel
from Orange.widgets.utils.state_summary import format_summary_details
from Orange.widgets.utils.signals import Input, Output
from Orange.widgets.utils.widgetpreview import WidgetPreview
