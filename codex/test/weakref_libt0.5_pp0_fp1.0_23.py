import weakref

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkPixbuf
from gi.repository import GObject
from gi.repository import GtkSource
from gi.repository import Pango

from pychess.System import conf
from pychess.System import glock
from pychess.System import uistuff
from pychess.System.idle_add import idle_add
from pychess.System.Log import log
from pychess.Utils.const import *
from pychess.Utils.Move import parseAN
from pychess.Utils.lutils.LBoard import LBoard
from pychess.Utils.lutils.lmove import parseSAN, toSAN
from pychess.Utils.lutils.lmovegen import genAllMoves
from pychess.Utils.Move import parseAny, toAN
from pychess.widgets.ChessFile import parse_game_result, parse_game_moves
