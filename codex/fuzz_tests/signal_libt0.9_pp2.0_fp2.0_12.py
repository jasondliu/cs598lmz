import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import logging
logger = logging.getLogger('mapclient.plugins.runfreesurfer')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

import mapclient.tools.pmap as pmap
import os
import subprocess
import shutil
import tempfile

from msl.qt import QtGui, QtWidgets
from msl.qt.application import Application

from .core.runfreesurfer import RunFreeSurfer
from .core.utils import settings, resetSettings
from .core.utils.settings import loadSettings, saveSettings
from .core.utils.version import getFSVersion, getFSVersionNumber
from .core.utils.colortable import getLutRgb
from .core.utils.runner import startProcess, SignallingProcess
from .core.utils.trackextractreconall import TrackExtractReconAll, \
    TrackExtractReconAllDlg, TrackExtractReconAllD
