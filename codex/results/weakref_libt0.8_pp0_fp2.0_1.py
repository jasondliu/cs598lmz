import weakref, new

from . import ui_embedding
from . import ui_utils

from .ui_utils import _, ungettext
from .utils.i18n import get_translation

from .utils.dictionary import GetDictionary
from .utils.manager import ActionManager
from .utils.manager import Manager, ManagerPage
from .utils.filelock import LockFile
from .utils.log import logger
from .utils.cursor import CursorManager
from .plugins import PluginMount
from .plugins.hooks import Hook
from .plugins.hooks import HookPoint
from .plugins.hooks import MenuHook
from .plugins.hooks import ContextMenuHook
from .plugins.hooks import SubContextMenuHook
from .plugins.hooks import SubMenuHook, DynamicMenuHook, ActionHook
from .plugins.hooks import PageHook
from .plugins.hooks import OptionsHook
from .plugins.hooks import SystemMenuHook
from .plugins.hooks import ToolbarHook
from .plugins.hooks import EditorHook, ViewerHook, EditorOpened
