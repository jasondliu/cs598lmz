import weakref

import gtk
import gobject

from pida.core.environment import get_version
from pida.core.environment import is_interactive

from pida.core.options import options

from pida.core.service import Service
from pida.core.features import FeaturesConfig, FeaturesPlugin
from pida.core.commands import CommandsConfig, CommandsPlugin

from pida.core.log import Log
from pida.core.events import EventsConfig
from pida.core.actions import ActionsConfig
from pida.core.actions import TYPE_NORMAL, TYPE_MENUTOOL, TYPE_MENU
from pida.core.actions import TYPE_RADIO, TYPE_TOGGLE
from pida.core.actions import TYPE_REMEMBER_TOGGLE, TYPE_REMEMBER_RADIO
from pida.core.actions import TYPE_REMEMBER_MENU
from pida.core.actions import IMG_MENU, IMG_MENUTOOL, IMG_MENUCHECK, IMG_MENURADIO
from pida.core.actions import IMG_
