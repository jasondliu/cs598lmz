import mmap
import os
import re
import shutil
import sys
import tempfile
import time

from distutils.version import LooseVersion

from avocado.core import exit_codes
from avocado.core import test
from avocado.core import exceptions
from avocado.utils import archive
from avocado.utils import process
from avocado.utils import distro
from avocado.utils import wait
from avocado.utils import path as utils_path
from avocado.utils import service


if sys.version_info[0] == 2:
    string_types = basestring,
else:
    string_types = str,


def _get_distro_version():
    """
    Gets the distro version from the system

    :return: the distro version
    """
    return distro.detect().version_number


def _get_distro_id():
    """
    Gets the distro id from the system

    :return: the distro id
    """
    return distro.detect().name


class VirtTest(test.Test):

    """
    Base class for all virt tests.

