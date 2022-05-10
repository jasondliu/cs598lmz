import gc, weakref
import os
import numpy as np
import time

import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets

from xicam.core.intents import Intent
from xicam.core.msg import logMessage
from xicam.core.threads import QtThreadExecutor
from xicam.core.data import NonDBHeader
from xicam.core.workspace import NonDBHeaderManager, NonDBHeaderCatalog

from .models import (NXattrsModel, NXdatasetsModel, NXdatasetsCatalogModel,
                     NXattributesCatalogModel, NonDBHeaderModel,
                     NonDBHeadersSourceModel, NonDBHeadersSinkModel)

from .views import (NXattrsView, NXdatasetsView, NXdatasetsCatalogView,
                    NXattributesCatalogView, NonDBHeaderView,
                    NonDBHeadersSourceView, NonDBHeadersSinkView)

from xicam.gui.static import path as gui_path


class HDF5Widget(QtWidgets.Q
