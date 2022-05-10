import weakref
import re
from datetime import datetime

import tornado.web
import tornado.escape

from qiita_core.qiita_settings import qiita_config
from qiita_core.qiita_settings import r_client
from qiita_db.util import get_count
from qiita_db.user import User, UserLevel
from qiita_db.logger import LogEntry
from qiita_db.study import Study
from qiita_db.exceptions import (QiitaDBUnknownIDError, QiitaDBDuplicateError)
from qiita_db.analysis import Analysis
from qiita_pet.handlers.api_proxy.util import (
    get_visibilities, get_processing_status, get_job_status)
from qiita_pet.handlers.api_proxy.oauth2 import authorized

# -----------------------------------------------------------------------------
# Helper methods
# -----------------------------------------------------------------------------
def get_user_studies(user):
    """Returns the studies for the provided user

    Parameters
    ----------
    user : User object
        The user
