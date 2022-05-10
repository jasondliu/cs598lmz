import gc, weakref, re
from uiutil import ChildWindow, BaseDialog
from uiutil.tk_names import EW, NS, ITALIC_FONT, NORMAL_FONT
from . import fonts
from .key_bindings import GlobalData

log = logging.getLogger(__name__)


class MappingTable(object):
    '''
    This class is an abstraction of a table of mapping pairs.
    '''

    def __init__(self, header_names):
        self.header_names = header_names
        self.entries = []
        self.bindings = {}

        for key in self.header_names:
            self.bindings[key] = []

    def __iter__(self):
        for i in self.entries:
            yield i
        raise StopIteration

    def __getitem__(self, index):
        return self.entries[index]

    def __len__(self):
        return len(self.entries)

    def clear(self):
        self.entries = []
        [i.clear() for i
