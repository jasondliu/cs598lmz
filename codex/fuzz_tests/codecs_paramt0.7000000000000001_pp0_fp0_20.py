import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Local imports
from . import utils
from . import config

# Constants
PLUGIN_DIR = 'plugins'
PLUGIN_INIT_FILE = '__init__.py'
PLUGIN_SUBDIRS = ['', 'gui', 'tools']
INIT_FILE_CONTENTS = '''# -*- coding: utf-8 -*-
"""
    {0}
    ~~~~~

    {1}
"""

__version__ = "{2}"

from .{3} import {4}
'''


@click.group()
@click.option('--debug/--no-debug', help="Enable debug mode", default=False)
@click.option('--quiet/--no-quiet', help="Enable quiet mode", default=False)
@click.option('--traceback/--no-traceback',
              help="Enable traceback display", default=False)
def cli(debug, quiet, traceback):
    """
    Command line utility for creating and managing plugins
    """

