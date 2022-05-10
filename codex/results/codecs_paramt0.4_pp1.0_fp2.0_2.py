import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Default configuration files
DEFAULT_CONFIG_FILE = 'config.yml'
DEFAULT_CONFIG_DIR = '.config/pip'
DEFAULT_CONFIG_FILE_OLD = 'pip.conf'

# Environment variables
PIP_CONFIG_ENV = 'PIP_CONFIG_FILE'
PIP_CONFIG_HOME_ENV = 'PIP_CONFIG_HOME'

# Configuration file names
PIP_CONFIG_FILE = 'pip.conf'
PIP_CONFIG_FILE_OLD = 'pip.ini'

# Configuration file sections
GLOBAL_CONFIG_FILE_SECTION = 'global'

# Configuration file options
INDEX_URL_OPTION = 'index-url'
INDEX_URL_OPTION_OLD = 'index-url'

class ConfigOptionParser(optparse.OptionParser):
    """
    Subclass of OptionParser which adds an option for a config file
    """
    def __init__(self, *args, **kwargs):

