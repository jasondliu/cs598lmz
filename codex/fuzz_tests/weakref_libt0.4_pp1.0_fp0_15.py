import weakref

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from . import config
from . import utils
from . import exceptions
from . import errors
from . import models

logger = logging.getLogger(__name__)


class Database(object):
    """
    Database connection.
    """

    def __init__(self, host=None, port=None, username=None, password=None,
                 db_name=None, ssl=False, ssl_ca_certs=None,
                 ssl_certfile=None, ssl_keyfile=None, ssl_pem_passphrase=None,
                 ssl_match_hostname=True, ssl_cert_reqs=ssl.CERT_NONE,
                 ssl_crlfile=None, ssl_ciphers=None,
                 replicaset=None, read_preference=None,
                 max_pool_size=None, min_pool_size=None,
                 max_idle_time_ms=None, wait_queue
