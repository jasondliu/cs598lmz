import mmap
import os

from . import config
from . import utils


def get_config_file():
    """
    Returns the full path to the configuration file.
    """
    return os.path.join(os.path.expanduser('~'), config.CONFIG_FILE)


def get_config_data(key):
    """
    Returns the data from the configuration file.

    :param key: The key to return
    :type key: str
    """
    config_file = get_config_file()
    if os.path.exists(config_file):
        with open(config_file) as f:
            try:
                data = json.load(f)
                return data.get(key, None)
            except ValueError:
                return None


def set_config_data(key, value):
    """
    Sets the data in the configuration file.

    :param key: The key to set
    :type key: str
    :param value: The value to set
    :type value: str
    """
    config_file = get_
