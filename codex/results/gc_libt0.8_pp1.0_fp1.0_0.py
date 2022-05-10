import gc, weakref, os, sys, time
import cPickle,  operator, itertools

import gtk, gobject, cairo

from pychess.System import glock, uistuff
from pychess.System.glock import glock_connect
from pychess.System.Log import log
import pychess.System.protoopen as protoopen

from pychess.Utils.const import *
import pychess.Utils.logic as logic
import pychess.Utils.Move as Move
import pychess.Utils.Eval as Eval
import pychess.Utils.Cord as Cord
import pychess.Utils.notation as notation
import pychess.widgets.Background

__title__ = _("Graphical Board")

__icon__ = "x-office-spreadsheet"

__desc__ =  _("Watch and analyze PGN games")

__longdesc__ = _("The board shows you PGN games graphically, allowing you to play through games, " +
                 "re-calculate variations, analyze positions, etc")
