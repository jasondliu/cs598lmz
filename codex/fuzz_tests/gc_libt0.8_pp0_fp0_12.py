import gc, weakref

from . import as_list
from .uri_helpers import uri_to_path, unparse_uri, uri_to_fs_path, parse_dir_uri
from .__version__ import __version__

from ._atom_table import _atom_table
from ._clipboard import Clipboard
from ._required_modules import _required_modules
from ._command import Command, _command_table
from ._event import Event, EventListener
from ._observable import Observable
from ._selection import Selection
from ._settings import Settings
from ._utils import _singleton
from ._window import Window
from ._workspace import Workspace
from ._kernel_client import KernelClient

_log = logging.getLogger(__name__)
_loaded = False

_registered_sessions = []
_session_table = {}
_session_listeners = []

_workspaces = []
_workspaces_listener = []

_instances = []
_instances_listener = []


def get_loaded_instances():
    return [i.data for i in _instances]
