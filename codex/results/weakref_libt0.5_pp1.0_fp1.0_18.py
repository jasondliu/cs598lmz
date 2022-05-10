import weakref
from collections import defaultdict
from collections import namedtuple
from functools import partial

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from core.util import get_main_window, get_ui_file
from core.util import get_setting
from core.util import set_setting
from core.util import open_file_browser

from core.log import getLogger
from core.node_manager import NodeManager
from core.node_manager import NodeManagerError
from core.node_manager import NodeManagerErrors
from core.node_manager import NodeManagerSignals
from core.node_manager import NodeManagerSignalNames
from core.node_manager import NodeManagerSignalArgs
from core.node_manager import NodeManagerSignalArgsNames
from core.node_manager import NodeManagerSignalArgsTypes
from core.node_manager import NodeManagerSignalArgsDescriptions
from core.node_manager import NodeManagerSignalArgsDefaults
from core.node_manager import NodeManagerSignalArgsUnits
from core.node_manager import NodeManagerSignal
