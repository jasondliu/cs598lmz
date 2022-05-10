import weakref

from . import helper
from . import major


class ClientArea(gtk.EventBox, object):
    '''
    The client area, which host the document and readline.
    '''
    __gtype_name__ = 'ClientArea'

    __gsignals__ = {
        # Emacs
        'query-substitute': (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, ()),
        'query-replace': (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, ()),
        'emacs-startedit': (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, ()),
        'emacs-endedit': (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, ()),
        'emacs-prepareedit': (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, ()),
        'emacs-edit-done': (gobject.SIGNAL_RUN_LAST,
