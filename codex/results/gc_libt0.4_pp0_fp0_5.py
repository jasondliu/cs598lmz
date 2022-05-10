import gc, weakref
import gtk, gobject
import pango

from sugar.graphics import style
from sugar.graphics.icon import Icon
from sugar.graphics.palette import Palette
from sugar.graphics.tray import TrayButton

import logging
_logger = logging.getLogger('read-toolbar')

_BORDER_WIDTH = style.LINE_WIDTH

_ZOOM_BUTTON_SIZE = style.zoom(48)
_ZOOM_BUTTON_PADDING = style.zoom(6)

_ZOOM_IN_ICON = 'zoom-in'
_ZOOM_OUT_ICON = 'zoom-out'

_ZOOM_IN_LABEL = _('Zoom in')
_ZOOM_OUT_LABEL = _('Zoom out')

_ZOOM_IN_TOOLTIP = _('Zoom in')
_ZOOM_OUT_TOOLTIP = _('Zoom out')

class ReadToolbar(gtk.Toolbar):

   
