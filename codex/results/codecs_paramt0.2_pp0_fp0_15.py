import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import utils
from . import config
from . import log
from . import exceptions

from . import __version__

logger = log.get_logger(__name__)

# -----------------------------------------------------------------------------
#
# -----------------------------------------------------------------------------

def _get_config_file():
    """
    Return the path to the configuration file.
    """
    return os.path.join(utils.get_config_dir(), 'config.yaml')

# -----------------------------------------------------------------------------
#
# -----------------------------------------------------------------------------

def _get_config_defaults():
    """
    Return the default configuration.
    """
    return {
        'version': __version__,
        'logging': {
            'level': 'info',
            'file': '',
        },
        'database': {
            'path': '',
        },
        'server': {
            'host': 'localhost',
            'port': 8080,
        },
        'client': {
            'host': 'localhost',
            'port': 8080,
        },
