import gc, weakref
from collections import defaultdict
import logging
from concurrent.futures import ThreadPoolExecutor

from gi.repository import GObject as gobject
from gi.repository import Gtk as gtk
from gi.repository import Gdk as gdk
from gi.repository import GdkPixbuf as gdkpixbuf
from gi.repository import GtkSource as gtksource
from gi.repository import Pango

from .util import get_builder
from .util import get_user_font
from .util import get_user_font_family
from .util import get_user_font_size
from .util import get_user_font_weight
from .util import get_user_font_style
from .util import get_user_font_variant
from .util import get_user_color_scheme
from .util import get_user_tab_width
from .util import get_user_show_line_numbers
from .util import get_user_show_right_margin
from .util import get_user_
