import weakref
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qsci import QsciScintilla, QsciLexerPython

import numpy as np

from spyder.config.base import _
from spyder.config.gui import get_color_scheme
from spyder.config.manager import CONF
from spyder.py3compat import to_text_string
from spyder.utils import icon_manager as ima
from spyder.utils import sourcecode
from spyder.utils.qthelpers import create_action
from spyder.utils.environ import EnvDialog
from spyder.utils.misc import getcwd_or_home
from spyder.widgets.variableexplorer import collectionseditor
from spyder.widgets.variableexplorer.collectionseditor import (
        RemoteCollectionsEditor)
from spyder.widgets.externalshell.monitor import MonitorWidget
from spyder.widgets.externalshell.threads import ThreadsWidget
from spyder.widgets.externalshell.names
