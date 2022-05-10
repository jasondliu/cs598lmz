import types
types.tuple = tuple

import sys
import glob

from . import fileperm as perm
from . import collect_feed_data as collect
from . import config as cfg
from . import logger


conf = cfg.load()
app = Flask(__name__)
app.config.update(conf)

BASE = conf['base']

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
sys.path.insert(0, SITE_ROOT)


lgr = logger.get_logger('webpage')


def add_timestamp(seed, clean=False):
    """
    Returns a string in form DATESTAMP_TIMESTAMP_SEED.
    Per default two underscores will be prepended
    """
    if clean:
        return '{0}_{1}_{2}'.format(dt.now().strftime('%Y%m%d'),
                                    dt.now().strftime('%H%M%S'),
                                    seed)
