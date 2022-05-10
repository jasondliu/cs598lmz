import weakref

from gi.repository import Gdk, GObject, Gtk, Pango

from pychess.System import conf, uistuff
from pychess.System.idle_add import idle_add
from pychess.System.prefix import addDataPrefix
from pychess.Utils.lutils.LBoard import LBoard
from pychess.Utils.lutils.lmove import parseSAN, toSAN
from pychess.Utils.lutils.lmovegen import genAllMoves, genCheckEvasions
from pychess.Utils.lutils.lmovegen import genCaptures, genNonCaptures
from pychess.Utils.lutils.lmovegen import genCheckEscapes, genEvasions
from pychess.Utils.lutils.lmovegen import genCheckers, genKingCaptures
from pychess.Utils.lutils.lmovegen import genCheckMoves, genQuietChecks
from pychess.Utils.lutils.lmovegen import genPseudoLegalMoves, genLegalMoves
