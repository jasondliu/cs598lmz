import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import utils
from . import config
from . import logger
from . import exceptions
from . import settings
from . import constants
from . import __version__

from .utils import get_version
from .utils import get_version_tuple
from .utils import get_version_number
from .utils import get_version_string
from .utils import get_version_timestamp
from .utils import get_version_timestamp_string
from .utils import get_version_timestamp_tuple
from .utils import get_version_timestamp_number
from .utils import get_version_timestamp_isoformat
from .utils import get_version_timestamp_isoformat_string
from .utils import get_version_timestamp_isoformat_tuple
from .utils import get_version_timestamp_isoformat_number
from .utils import get_version_timestamp_utc_isoformat
from .utils import get_version_timestamp_utc_isoformat_string
from .utils import get_version_timestamp_utc_iso
