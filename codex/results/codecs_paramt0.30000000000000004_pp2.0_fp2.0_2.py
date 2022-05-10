import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import __version__

from . import config
from . import utils
from . import log
from . import log_utils
from . import db
from . import db_utils
from . import web
from . import web_utils
from . import web_utils_db
from . import web_utils_common
from . import web_utils_security
from . import web_utils_download
from . import web_utils_upload
from . import web_utils_scheduler
from . import web_utils_torrent
from . import web_utils_rss
from . import web_utils_notifications
from . import web_utils_search
from . import web_utils_history
from . import web_utils_postprocess
from . import web_utils_manage
from . import web_utils_manage_torrent
from . import web_utils_manage_rss
from . import web_utils_manage_search
from . import web_utils_manage_history
from . import web_utils_manage_postprocess
from . import
