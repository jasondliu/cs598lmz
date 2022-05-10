import weakref

import kaa
import kaa.notifier
import kaa.display
import kaa.input
import kaa.cui
import kaa.geometry
import kaa.keys
import kaa.evlist

if sys.version_info >= (3, 0):
    def ascii_ord(c):
        return ord(c)
else:
    def ascii_ord(c):
        if isinstance(c, str):
            return ord(str(c))
        else:
            return c


