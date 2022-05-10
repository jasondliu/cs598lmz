import weakref

from panda3d.core import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.showbase.PythonUtil import *
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.fsm import StateData
from direct.directnotify import DirectNotifyGlobal
from direct.task.Task import Task
from direct.showbase import AppRunnerGlobal
from direct.showbase import MessengerLeakDetect
from direct.showbase.PythonUtil import report
from otp.otpbase import OTPGlobals
from otp.otpbase import OTPLocalizer
from otp.otpbase import OTPLauncherGlobals
import sys
import os
import __builtin__
import random
import time
import webbrowser
import string
import re
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.gui import DirectGuiGlobals
from otp.launcher import DownloadForceAcknowledge
