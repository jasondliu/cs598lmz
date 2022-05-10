import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import subprocess
import threading
import re
import json
import math
import datetime
import traceback

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebChannel import *

from . import utils
from . import config
from . import settings
from . import dialogs
from . import resources
from . import webview
from . import webchannel
from . import webchannel_bridge
from . import webchannel_handler
from . import webchannel_handler_bridge
from . import webchannel_handler_bridge_qt
from . import webchannel_handler_bridge_qt_bridge
from . import webchannel_handler_bridge_qt_bridge_bridge
from . import webchannel_handler_bridge_qt_bridge_bridge_bridge
from . import webchannel
