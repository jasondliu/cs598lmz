import mmap
import os
import re
import sys

try:
    import cPickle as pickle
except ImportError:
    import pickle

from cStringIO import StringIO

from pkgcore.config import basics, configurable
from pkgcore.ebuild.cpv import CPV
from pkgcore.fs import livefs
from pkgcore.log import logger
from pkgcore.package import errors
from pkgcore.package.metadata import package_factory
from pkgcore.restrictions import packages
from pkgcore.restrictions.boolean import OrRestriction
from pkgcore.restrictions.util import collect_package_restrictions
from pkgcore.test import TestRestriction
from pkgcore.util import commandline
from pkgcore.util.file_type import directory

from snakeoil.demandload import demandload
demandload(globals(),
    'errno:os',
    'logging',
    'os.path',
    'pkgcore:osutils',
    'snakeoil.osutils:pjoin',
    '
