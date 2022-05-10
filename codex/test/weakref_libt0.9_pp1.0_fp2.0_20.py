import weakref
from collections import OrderedDict

from kivy.app import App
from kivy.logger import Logger
from kivy.uix.button import Button
from kivy.uix.screenmanager import FadeTransition, ScreenManager, Screen
from kivy.properties import ListProperty, NumericProperty, BooleanProperty,\
    ObjectProperty, StringProperty, DictProperty, BoundedNumericProperty


from market.market_item import MarketItemList, MarketItem
from market.market_filter import AllowedItemFilter, ShipItemFilter
from market.market_database import MarketDB
from market.market_price import PriceDatabase
from market.market_category import CategoryDatabase

from ship.ship import Ship
from ship.ship_ui import ShipView


from equipment.equipment_entry import EquipmentEntry
from equipment.equipment_providers import EquipmentDatabaseSingleton


class CategoryButton(Button):
    pass


class CategoryListMember(Button):
    item_id = NumericProperty(0)
    # Index of item selected
    item_index = NumericProperty(0)

