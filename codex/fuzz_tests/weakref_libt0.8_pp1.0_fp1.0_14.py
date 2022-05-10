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


@validate_config(
    ('service', is_string_instance),
    ('password', is_string_instance),
    ('user', is_string_instance),
    ('user_handler', ()),
)
def pam_authenticator(driver, config):
    """Create a PAMAuthenticator instance.

    Parameters
    ----------
    driver: GatherDriver
    config: dict-like
        This is a dict-like object
