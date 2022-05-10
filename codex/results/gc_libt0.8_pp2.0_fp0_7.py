import gc, weakref

from pychess.Utils.const import *
from pychess.Utils.lutils.ldata import *
from pychess.Utils.lutils.lmove import *
from pychess.Utils.lutils.LBoard import LBoard
from pychess.Variants.suicide import SuicideBoard

from pychess.Utils.lutils.leval import getPieceValue
from pychess.Utils.lutils.lsearch import (
    alphaBetaMin,
    alphaBetaMax,
    principalVariation,
)
from pychess.Utils.lutils.lmovegen import (
    genAllMoves,
    genCaptures,
    genNonCaptures,
    genCheckEvasions,
    genCheckEvasionsNonCapturing,
)
from pychess.Utils.lutils.lbitboard import popCount
from pychess.Utils.lutils.lmove import listToSan
from pychess.Utils.lutils.lmove import moveToSAN
from pychess.Utils.lutils
