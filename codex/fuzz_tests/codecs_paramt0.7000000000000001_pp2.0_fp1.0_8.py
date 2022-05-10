import codecs
codecs.register_error('strict', codecs.ignore_errors)
import sys
from glob import glob
from optparse import OptionParser

from .. import __version__
from .. import util
from .. import __main__
from .. import db
from .. import cache
from .. import opts
from .. import context
from .. import hook
from .. import errors
from .. import pkgcore_checksum
from .. import repo_objs
from .. import repo_utils
from .. import os_data
from .. import ebd
from .. import atom
from .. import cpv

from ..repo_objs import repo_pkg

from ..config import parser as config_parser

from ..console_output import darkgreen, red, blue, bold, darkred, brown
from ..output import bold, TextPrinter, TextProgressBar
from ..version_compare import vercmp, _pkg_str
from ..ebd.format import format_ebuild_msg, format_changes
from ..cache.mappings import bidict, inverse_dict
from ..cache.flat_hash import cache_checksum
from ..fetcher import fetchable as fetch

