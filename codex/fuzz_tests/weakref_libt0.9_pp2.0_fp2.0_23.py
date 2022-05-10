import weakref

from gi.repository import GObject, GLib, GdkPixbuf, Gtk, EvinceDocument, \
    EvinceView
from Onboard.utils import Rect, open_url
import Onboard.OnboardErrors as OnboardErrors

import Onboard.Layout      as Layout
import Onboard.Keyboard    as Keyboard
import Onboard.KeyGtk      as KeyGtk
import Onboard.KeyEvents   as KeyEvents
import Onboard.OSK         as OSK
import Onboard.WindowUtils as WindowUtils
import Onboard.InputLine   as InputLine
import Onboard.Volume      as Volume
import Onboard.Mouse       as Mouse
import Onboard.config      as config
import Onboard.scim        as scim
import Onboard.xutils      as xutils
import Onboard.AutoHide    as AutoHide

### Logging ###
import logging
_logger = logging.getLogger("LayoutManager")
###############

LAYOUT_GROUPS_MMAP = ("[", "]", "(", ")", "{", "}", "<
