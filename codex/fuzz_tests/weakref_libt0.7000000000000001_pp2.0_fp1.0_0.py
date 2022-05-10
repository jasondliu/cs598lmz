import weakref
import sys
import atexit
import os
import re
import shutil
import subprocess
import logging
import textwrap
import codecs
import six

from argparse import (ArgumentParser, _SubParsersAction, _SubParsersAction,
                      _SubParsersAction, _VersionAction)
import pkg_resources

from .config import (Project, FileSettings, ListOption, DictOption,
                     BoolOption, Option, IntOption, StrOption)
from . import pkgdeps, util, sphinx_ext, conf
from . import __version__
import jb_common

logger = logging.getLogger(__name__)

class ConfigError(Exception):
    """Exception for configuration related errors"""

class Project(Project):
    """A project is a collection of configuration settings"""

    #: The project type
    project_type = 'sphinx'

    #: Enable the sphinx extension
    sphinx = BoolOption(True)

    #: The project's source directory
    source_dir = Option(util.default_
