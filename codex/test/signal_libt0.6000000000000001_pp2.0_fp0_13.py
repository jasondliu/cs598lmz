import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk, GObject

from pychess.System import conf
from pychess.System import uistuff
from pychess.System.prefix import addDataPrefix

from pychess.Players.Human import Human
from pychess.Players.Human import get_type
from pychess.Players.Human import get_engine_dict
from pychess.Players.Human import get_display_text

from pychess.Utils.IconLoader import load_icon, get_pixbuf
from pychess.Utils.const import *
from pychess.Utils.Move import parseAN
from pychess.Utils.Offer import Offer, TakebackOffer, DrawOffer, AdjournOffer, AbortOffer, SwitchOffer
from pychess.Utils.logic import validate
from pychess.Utils.Move import Move
from pychess.Utils.lutils.lmovegen import newMove
