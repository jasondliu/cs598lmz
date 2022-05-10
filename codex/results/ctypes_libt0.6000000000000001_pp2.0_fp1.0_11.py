import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from . import config
from . import util
from . import config_window
from . import main_window
from . import data_window
from . import graph_window
from . import network_window
from . import search_window
from . import search_result_window
from . import data_edit_window
from . import config_window
from . import data_manager
from . import data_manager_window
from . import graph_manager
from . import graph_manager_window
from . import graph_manager_window_tabs
from . import graph_manager_window_tabs_single
from . import graph_manager_window_tabs_multiple
from . import graph_manager_window_tabs_threshold
from . import graph_manager_window_tabs_up_down
from . import graph_manager_window_tabs_group
from . import graph_manager_window_tabs_group_single
from . import graph_manager_window_tabs_group_multiple
from . import graph_manager_window_tabs_group_th
