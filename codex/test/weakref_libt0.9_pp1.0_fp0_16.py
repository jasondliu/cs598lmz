import weakref

from gui.Scaleform.manager.SoundManager import g_soundManager

from gui.shared.gui_items import GUI_ITEM_TYPE
import items
from gui.shared.ItemsCache import g_itemsCache

from skeletons.gui.game_control import IBrowserController, ITradeInController, ISoundController
from skeletons.gui.shared import IItemsCache

_BACK_LOADER_PATH = '../maps/icons/filters/functions_back.png'
_BACK_ICON_PATH = '../maps/icons/filters/connoisseurs_back.png'
_TOOLTIP_HEADER = 'tradeIn/'

class TRADE_IN_TAB_TYPE(object):
    DEFAULT_VIEW = 0
    TC130 = 1


class TradeInController(ITradeInController):
    __itemsCache = dependency.descriptor(IItemsCache)
    __soundCtrl = dependency.descriptor(ISoundController)

    def __init__(self):
        super(TradeInController, self).__init__()
