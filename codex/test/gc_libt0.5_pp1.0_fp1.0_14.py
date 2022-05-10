import gc, weakref

# ------------------------------------------------------------------------------
# ---[ Constants ]--------------------------------------------------------------
# ------------------------------------------------------------------------------

_config = {
    'default': {
        'port': 8080,
        'host': '0.0.0.0',
        'debug': True,
        'autoreload': True,
        'server': 'tornado',
    },
}

_config_file = None
_config_override = None

# ------------------------------------------------------------------------------
# ---[ Functions ]--------------------------------------------------------------
# ------------------------------------------------------------------------------

def _reload_config():
    """ Reloads the configuration from the config file. """
    global _config_file, _config_override
    _config_file = None
    _config_override = None

def _get_config():
    """ Returns the configuration. """
    global _config_file, _config_override
    if _config_file is None:
        _config_file = {}
        _config_override = {}
        # The config file is located in the root directory of the project.
