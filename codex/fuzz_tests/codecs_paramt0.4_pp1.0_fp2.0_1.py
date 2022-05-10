import codecs
codecs.register_error('strict', codecs.ignore_errors)

# TODO: this is a hack.
# We need to find a way to remove the dependency on the
# directory structure.
#
# This is a list of directories that are searched for
# modules.
sys.path.extend(['.', './lib', '../lib', '../../lib'])

import logging
import logging.config

from optparse import OptionParser

import config

from pylons import config as pylons_config
from pylons import app_globals as g
from pylons.i18n.translation import _get_translator

from r2.lib.db import tdb_cassandra
from r2.lib.db.tdb_sql import init_db_sessions

from r2.models import *
from r2.models.subreddit import DefaultSR
from r2.models.wiki import WikiPage
from r2.models.token import OAuth2Client
from r2.models.token import OAuth2AccessToken
from r2.models.token import OAuth2
