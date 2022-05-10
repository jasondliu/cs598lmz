import select
import sys
import time
import os
import re
import subprocess
import threading
from datetime import datetime

from . import log
from . import utils
from . import exceptions
from . import config

def get_default_editor():
    env_editor = os.environ.get('EDITOR')
    editor = env_editor or os.environ.get('VISUAL') or 'vim'
    return editor

def get_editor():
    return config.get('editor', get_default_editor())

def run_editor(text=None, file=None, extension=None, wait=True):
    """Run the editor.

    :param text: the text to edit
    :param file: the file to edit
    :param extension: the extension to use for the temporary file
    :param wait: whether to wait for the editor to finish
    :returns: the edited text
    """
