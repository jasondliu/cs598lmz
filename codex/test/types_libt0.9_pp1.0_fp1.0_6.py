import types
types.coerce_timestamp = lambda x: x

import gnome
from gnome.services import *
from gnome.services.helplib import _have_reference_help
from gnome.services.jokes import _have_pyjokes
from gnome.services.schemaupdater import schemademo
from gnome.services.wotd import wotd

sys.path.append('../gnome/ui')
from ui import GnomeApp, NULL, print_w, print_

gconf = Config.init()

AVAILABLE_SERVICES = [('xkcd', xkcd),
                      ('calculator', calcop),
                      ('a', oxford),
                      ('p', pyglossary),
                      ('j', pyjokes),
                      ('h', refbrowser),
                      ('w', wotd)]

class DummyGladeApp(GnomeApp):
    def __init__(self):
        GnomeApp.__init__(self)
        self.services = {}
