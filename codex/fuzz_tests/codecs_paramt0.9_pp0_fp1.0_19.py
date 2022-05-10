import codecs
codecs.register_error('strict', codecs.ignore_errors)
from aqt import mw
from aqt.utils import showInfo,tooltip
from aqt.qt import *
from anki import notes
import aqt
from .loadnote import *
import re
from aqt.browser import Browser
from .config import getUserOption
from .myutils import getFieldNamesFromModel, getFieldList
from .kanji_for_cards import KanjiForCards

from ..constants import *

from .Dialogs.classcommanote import *

from kanji_for_cards.decorators import allow_one_instance_per_deck
from kanji_for_cards.myutils.string_utils import is_kanji


from unidecode import unidecode
def SJISDecode(x):
    return x.decode('cp932', 'strict')
def SJISEncode(x):
    return x.encode('cp932', 'strict')
def cp932Len(x):
    return len(x.encode('cp932', 'strict'))
