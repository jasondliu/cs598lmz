import weakref

from . import helper
from . import major


class ClientArea(gtk.EventBox, object):
    '''
    The client area, which host the document and readline.
    '''
    __gtype_name__ = 'ClientArea'

