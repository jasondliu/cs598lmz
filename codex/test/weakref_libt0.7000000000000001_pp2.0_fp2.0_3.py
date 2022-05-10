import weakref

import gtk

from sugar.graphics.icon import Icon
from sugar.graphics import style
from sugar.graphics.objectchooser import ObjectChooser
from sugar.graphics.xocolor import XoColor
from sugar.graphics.palette import Palette
from sugar.graphics.palettemenu import PaletteMenuBox
from sugar.graphics.toolbutton import ToolButton
from sugar.graphics.tray import HTray
from sugar.graphics.menuitem import MenuItem
from sugar.graphics.alert import NotifyAlert

import logging
_logger = logging.getLogger('JournalActivity')

from sugar.graphics import iconentry

import model

from gettext import gettext as _
import locale

class NotFoundAlert(NotifyAlert):
    def __init__(self, activity):
        NotifyAlert.__init__(self)

        self.props.title = _('Entry not found')
        self.props.msg = _('Sorry, the entry you were looking for '
                           'was not found.')

       
