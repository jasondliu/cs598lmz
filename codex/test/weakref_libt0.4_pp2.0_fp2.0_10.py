import weakref

from . import config
from . import log
from . import utils
from . import version

__all__ = [
    'Application',
    'ApplicationError',
    'ApplicationExit',
    'ApplicationExitError',
    'ApplicationNoConfigError',
    'ApplicationNoConfigFileError',
    'ApplicationNoConfigSectionError',
    'ApplicationNoConfigValueError',
    'ApplicationNoLogError',
    'ApplicationNoLogFileError',
    'ApplicationNoLogSectionError',
    'ApplicationNoLogValueError',
    'ApplicationNoVersionError',
    'ApplicationNoVersionFileError',
    'ApplicationNoVersionSectionError',
    'ApplicationNoVersionValueError',
    'ApplicationVersionError',
    'ApplicationVersionExitError',
    'ApplicationVersionExit',
]

logger = logging.getLogger(__name__)


class ApplicationError(Exception):
    """
    Base application error.
    """


class ApplicationNoConfigError(ApplicationError):
    """
    Raised when the application configuration is not available.
    """


