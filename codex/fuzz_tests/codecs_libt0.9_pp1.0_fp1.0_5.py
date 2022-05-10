import codecs
codecs.register_error('strictignore', codecs.ignore_errors)
import os
from requests.compat import urljoin
from . import configuration, builder, publisher
from . import console, util, exceptions, git, build
import shutil
from .util import log
from .logger import logger, setup_logger
from . import git
from .toml import TomlDecodeError, TomlEncodeError
from .client.client import Client, MethodNotAllowedError
from .configuration import ProjectConfig, get_project_config, set_project_config, get_config, set_config
from . import version
from . import download
from . import build_status
from .output import set_verbose
from .__main__ import main
from .version import __version__, __commit__


__all__ = [
    'upload',
    'init',
    'publish',
    'build',
    'configuration',
    'builder',
    'publisher',
    'console',
    'util',
    'exceptions',
    'git',
    'build',
   
