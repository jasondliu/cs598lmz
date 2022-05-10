import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import threading
import subprocess

from PyQt5.QtCore import *
from PyQt5.QtGui import *
