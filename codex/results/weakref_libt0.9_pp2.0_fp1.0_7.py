import weakref

import gtk

from mcomix import preport
from mcomix import i18n
from mcomix import constants
from mcomix import thumbnail_frame
from mcomix importThumbnailChooseDialog,ThumbnailGenerationDialog

def _(message): return i18n.to_unicode(message)

class ThumbnailSidebar(gtk.VBox):

    def __init__(self, window):

        gtk.VBox.__init__(self)

        self._window = weakref.proxy(window)

        self._thumbnail_frame = thumbnail_frame.ThumbnailFrame(self._window)
        self._thumbnail_frame.connect('request-open-path', self._open_path)
        self.pack_start(self._thumbnail_frame)

        toggle_thumbnail = gtk.Button(_('显示缩略图'))
        toggle_thumbnail.connect('clicked', self._toggle_thumbnails)
        toggle_thumbnail.set_tooltip_text(_('Enable/disable the showing of thumbnails.'))
        self
