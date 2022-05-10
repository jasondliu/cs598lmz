import types
types.__builtins__["_"] = _

import os
import re
import json
import shutil
import urllib
import zipfile
import glob
import hashlib
import subprocess

from collections import OrderedDict
from io import BytesIO
from urllib import request
from urllib.error import HTTPError, URLError

from . import utils, config
from . import dependencies_check
from . import installer_gui
from . import installer_gui_qt
from . import installer_gui_wx
from . import installer_gui_curses

from .utils import (
    decompress_file,
    remove_file,
    remove_dir,
    remove_file_safely,
    remove_dir_safely,
    copy_file,
    copy_tree,
    copy_file_safely,
    copy_tree_safely,
    init_dir,
    init_file,
    init_file_with_content,
    get_file_sha1,
    get_file_md5,
    get_file_size,

