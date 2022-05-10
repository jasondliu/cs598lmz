import lzma
lzma.LZMAError

import logging
logger = logging.getLogger(__name__)

import sys
import time
import tempfile
import shutil
import os
import os.path
import re
import subprocess
import json

from . import utils
from . import config
from . import commands
from . import schema

class Progress(object):
    """
    Progress reporting for the 'git-annex' command.
    """

    def __init__(self, annex):
        self.annex = annex

    def __call__(self, progress):
        """
        Progress reporting callback.

        :param progress: parsed progress information
        """
        if 'scanning' in progress:
            # Scanning progress
            repo = progress['scanning']
            if not repo:
                logger.warning("Scanning progress: no repository")
                return
            if 'scan_progress' in progress:
                # Scanning progress
                self.annex.repos[repo]['scan_progress'] = progress['scan_progress']
                if self.annex.status
