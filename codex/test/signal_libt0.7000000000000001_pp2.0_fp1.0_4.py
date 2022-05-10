import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk

from pychess.System import conf
from pychess.System import uistuff
from pychess.System import glock
from pychess.System import variant
from pychess.System import fident
from pychess.System.idle_add import idle_add
from pychess.System.prefix import addDataPrefix
from pychess.Utils.const import NORMALCHESS, FISCHERRANDOMCHESS, WILDCASTLESHUFFLECHESS
from pychess.Utils.const import isSaneBoard, VARIANTS_OTHER_NONSTANDARD
from pychess.Utils.Offer import Offer
from pychess.Utils.lutils import lsearch, lsearch_pos, lsort
from pychess.Utils.Move import parseAny

from .PromotionDialog import PromotionDialog
from .AnalysisDialog import AnalysisDialog
from .BoardView import BoardView

