import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Set up logging
logger = logging.getLogger(__name__)

# Set up module-level variables
DEFAULT_CONFIG_FILE = '~/.config/pypianoroll/pypianoroll.conf'
DEFAULT_CONFIG_SECTION = 'pypianoroll'

# Read config file
config = configparser.SafeConfigParser()
config.read(os.path.expanduser(DEFAULT_CONFIG_FILE))

# Set up module-level variables
if config.has_section(DEFAULT_CONFIG_SECTION):
    DEFAULT_MIDI_PATH = config.get(DEFAULT_CONFIG_SECTION, 'DEFAULT_MIDI_PATH')
    DEFAULT_MUSIC21_PATH = config.get(DEFAULT_CONFIG_SECTION, 'DEFAULT_MUSIC21_PATH')
    DEFAULT_MATPLOTLIB_PATH = config.get(DEFAULT_CONFIG_SECTION, 'DEFAULT_MATPLOTLIB_PATH')
   
