import weakref

from time import time, sleep

import lxml.etree
from lxml.builder import ElementMaker

from hotwire.builtin import Builtin
from hotwire.sysdep.fs import File, Dir
from hotwire.sysdep.proc import Executable, Signal
from hotwire.log import Logging
from hotwire.result import Result
from hotwire.util.timer import Timer

NAMESPACE = "http://hotwire.yavor.org/xml/preferences"
NSMAP = {
    'preferences': NAMESPACE
    }
E = ElementMaker(namespace=NAMESPACE, nsmap=NSMAP)

class Preferences(Logging):
    """The Preferences object provides the interface to the preferences
    system. Using this class, you can read and write preferences and
    register handlers to receive notification when preferences change.
    """
    
    def __init__(self):
        super(Preferences, self).__init__()
        self._handlers = {}

    def _call_handler(self, key, value):
        if key in
