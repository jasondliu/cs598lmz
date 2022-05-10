import weakref
import locale
import copy

import gtk
import pango
import gobject

from util.textutil import flatten, model_iter_to_list, get_markup_lines
from util.textutil import model_get_iter_first
from util.textutil import multiline_replace_regex, get_iter_at_line_pos
from util.textutil import gtktextiter_to_list

from util.common import current_time

from guicomponents import FileChooserDialog

from guicomponents import get_pangocairo_context

import logging
_logger = logging.getLogger('guicomponents.ChatTextView')
del logging

class ChatTextView(gtk.TextView, gobject.GObject):
    # pylint: disable-msg=W0622
    __gtype_name__ = 'SugarChatTextView'

    __gsignals__ = {
        #SENT by this object when the user hits <enter>
        'activate': (gobject.SIGNAL_RUN_LAST, gob
