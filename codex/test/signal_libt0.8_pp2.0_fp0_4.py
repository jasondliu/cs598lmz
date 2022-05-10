import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import Tkinter as tk

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),
    os.pardir)))
from controller.Game import Game
from controller.gui.TKGameState import TKGameState

import controller.gui.TKTeam as TKTeam
from controller.gui.TKRobot import TKRobot
from controller.gui.TKBall import TKBall
from controller.gui.TKObject import TKObject
from controller.gui.TKGoal import TKGoal
from controller.gui.TKField import TKField
from controller.gui.TKDrawableRectangle import TKDrawableRectangle
from controller.gui.TKDrawableEllipse import TKDrawableEllipse
from controller.gui.TKDrawableLine import TKDrawableLine
from controller.gui.TKDrawableText import TK
