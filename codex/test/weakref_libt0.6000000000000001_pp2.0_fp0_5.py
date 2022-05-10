import weakref
from gi.repository import GObject, Gtk
import logging

from sugar3.graphics import style
from sugar3.graphics.icon import Icon
from sugar3.graphics.xocolor import XoColor
from sugar3.graphics.palette import Palette
from sugar3.graphics.palettemenu import PaletteMenuBox
from sugar3.graphics.palettemenu import PaletteMenuItem
from sugar3.activity.widgets import ActivityToolbarButton

from jarabe.model import shell
from jarabe.model import network
from jarabe.model import volume
from jarabe.model.volume import VolumeWatcher
from jarabe.model import battery
from jarabe.journal import journalwindow
from jarabe.webservice import accountsmanager


_NETWORK_ICON = 'network-idle'
_BATTERY_ICON = 'battery'
_JOURNAL_ICON = 'journal'
_VOLUME_ICON = 'audio-volume-medium'
