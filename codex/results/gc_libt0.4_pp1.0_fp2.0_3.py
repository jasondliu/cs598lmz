import gc, weakref
import logging
import os
import random
import re
import sys
import threading
import time
import traceback
import types
import urllib

import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs

from . import gui
from . import guiutils
from . import kodigui
from . import util
from . import windowutils
from . import youtube

log = logging.getLogger('PLEX.dialogs')

# TODO: Remove this when we're ready to use the new dialogs.
USE_OLD_DIALOGS = False

# TODO: Remove this when we're ready to use the new dialogs.
if USE_OLD_DIALOGS:
    from . import olddialogs as dialogs
else:
    import dialogs

# TODO: Remove this when we're ready to use the new dialogs.
if USE_OLD_DIALOGS:
    from . import olddialogs as dialogs
else:
    import dialogs

# TODO: Remove this when we're ready to use the new dialog
