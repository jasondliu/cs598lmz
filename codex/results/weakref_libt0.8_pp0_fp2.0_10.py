import weakref

import numpy

from . import check_stack

from . import image, image_array
from . import plugins
from ._sort_plugins import sort_plugins
from . import data_wizard
from . import display_data


# Override for dynamic priority/visibility changes
def priority_visibility_changed_cb(plugin_class, pv_dict):
    # Loop through all open data windows
    for data_window in Data.data_windows:
        # Loop through all plugins
        for key in list(data_window.plugin_managers.keys()):
            # If it's opened, update
            if plugin_class == key:
                data_window.plugin_managers[key].priority_visibility_changed(
                    pv_dict)


def get_instance():
    """Return the singleton Data class."""
    return Data.instance

def get_data_window_list():
    """Return a list of open data windows."""
    return Data.data_windows

def register_data_window(data_window):
    """Register a DataWindow in the
