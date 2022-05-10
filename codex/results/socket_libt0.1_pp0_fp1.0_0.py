import socket
import sys
import time

from . import config
from . import log
from . import util
from . import version

logger = log.get_logger()


def get_version():
    return version.__version__


def get_version_info():
    return version.__version_info__


def get_version_string():
    return version.__version_string__


def get_version_date():
    return version.__version_date__


def get_version_commit():
    return version.__version_commit__


def get_version_branch():
    return version.__version_branch__


def get_version_tag():
    return version.__version_tag__


def get_version_info_string():
    return version.__version_info_string__


def get_version_info_date():
    return version.__version_info_date__


def get_version_info_commit():
    return version.__version_info_commit__


def get_version_info_branch():
    return version
