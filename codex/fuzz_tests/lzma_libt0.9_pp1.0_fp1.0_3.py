import lzma
lzma.open
BZ2File
"""

from command import Command
import sys
import os
import re
import traceback
import collections
import optparse
from zipfile import ZipFile, ZIP_DEFLATED
from configparser import ConfigParser
from shutil import copyfileobj
from tarfile import TarFile
import tempfile
from system import system
import command
import syslog
from getpass import getpass


class Package(Command):
    __doc__ = """
    The package command packages and extracts the files needed to make a 
    Pisi package.

    Usage: package [<version>]

    @version: <version> defaults to latest 'release' version.
              ( <version> must be a valid version tag in the local SCM repository )
    """

    def __init__(self):
        super().__init__()
        self._parser = optparse.OptionParser(usage=Package.__doc__)
        self._parser.add_option("-t", "--targz", action="store_true", dest="targz",
                            help="make a .tar.gz
