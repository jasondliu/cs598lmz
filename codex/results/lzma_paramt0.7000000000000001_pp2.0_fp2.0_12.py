from lzma import LZMADecompressor
LZMADecompressor = LZMADecompressor  # pylint: disable=invalid-name,redefined-outer-name

from google.cloud.ndb import _datastore_types
from google.cloud.ndb import _eventloop
from google.cloud.ndb import _options
from google.cloud.ndb import _utils
from google.cloud.ndb import context as context_module
from google.cloud.ndb import exceptions
from google.cloud.ndb import key as key_module
from google.cloud.ndb import model
from google.cloud.ndb import query as query_module
from google.cloud.ndb import tasklets

# pylint: disable=invalid-name
_MAX_XG_OPS = _options.Options.max_xg_tx_ops
_MAX_XG_SIZE = _options.Options.max_xg_tx_size
_MAX_PUT_OPS = _options.Options.max_put_ops
_MAX_PUT_SIZE = _options.Options.max_put_size
_MAX_GET_KEYS = _options.Options
