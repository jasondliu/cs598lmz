import types
types.FunctionType = lambda: None


from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
from otp.speedchat import SCColorScheme
from otp.speedchat import SCStaticTextTerminal
from otp.otpbase import OTPGlobals
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.toontowngui import TTDialog
from toontown.toonbase import ToontownBattleGlobals
from toontown.battle import Fanfare
from otp.otpbase import OTPLocalizer
from toontown.toontowngui import TeaserPanel
from toontown.toontowngui import TeaserPanel2
from otp.avatar import Avatar
