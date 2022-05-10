import weakref

from ..utils import get_logger
from ..utils import import_object
from ..utils import Strings
from ..utils import validate_config
from ..utils import validate_set
from ..utils import is_string_instance

from .base import BaseAuthenticator
from .base import UserHandler
from .base import UserInfo
from .base import User

_logger = get_logger(__name__)

_default_config = {
    'class': 'gather.authenticators.pam.PAMAuthenticator',
    'service': 'login',
    'password': 'secret',
    'user': 'gather'
}


