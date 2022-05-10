import weakref
from functools import partial
from typing import Callable, Dict, List, Optional, Tuple, Union

import numpy as np
import pandas as pd
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QCheckBox, QComboBox, QDialog, QLabel, QSpinBox, QVBoxLayout, QWidget
from PyQt5.uic import loadUi
from qtpy.QtCore import Slot
from qtpy.QtWidgets import QProgressBar

from PartSeg._channels.channels import Channel
from PartSeg._channels.channels_calc import ChannelCalc
from PartSegCore.algorithm_describe_base import AlgorithmProperty
from PartSegCore.analysis.calculate_all import CalculateAll, CalculateAllTask
