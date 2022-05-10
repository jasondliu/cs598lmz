import gc, weakref
import operator

from collections import OrderedDict
from blinker import NamedSignal, NamedMultipleSignals
from distutils.version import LooseVersion
from werkzeug.utils import cached_property
from werkzeug.local import LocalProxy

from .signals import NamespaceSignals
from .utils import _wp_to_hk_name
from .helpers import _flatten
from .ext import Record, Record_and_Action
from .ext.named_events import NamedEventManager
from .ext.events import EventManager
from .ext.hotkeys import Hotkey
from .ext.hotkey_helper import HotkeyHelper
from .ext.context_menu import MenuItem
from .ext.config import Config
from .ext.plugin_manager import PluginManager

__all__ = ['Extension', 'ExtensionManager', 'NamedExtension', 'NamedExtensionManager']


class ExtensionBase:
    """Base class for all extensions.

    An extension has to inherit from this class and has to implement the :meth:`on_load` and
    :meth:`on
