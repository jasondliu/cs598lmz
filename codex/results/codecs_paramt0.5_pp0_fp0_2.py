import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import __version__
from . import __author__

from . import config
from . import log
logger = logging.getLogger('pymdownx.githubemoji')

from . import util

try:
    import requests
except ImportError:
    logger.warning("Please install requests. See README for details.")
    logger.warning("Emoji support disabled.")
    requests = None

try:
    import yaml
except ImportError:
    logger.warning("Please install PyYAML. See README for details.")
    logger.warning("Emoji support disabled.")
    yaml = None

try:
    import json
except ImportError:
    logger.warning("Please install json. See README for details.")
    logger.warning("Emoji support disabled.")
    json = None

try:
    from markdown import Extension
except ImportError:
    logger.warning("Please install Markdown. See README for details.")
    logger.warning("Emoji support disabled.")
    Extension = None


