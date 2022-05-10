import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile

from . import _util
from . import _vendor
from . import _yaml
from . import _yaml_util
from . import _yaml_ordered_dict
from . import _yaml_ordered_dict_ext
from . import _yaml_ordered_dict_loader

# TODO(b/148972318): Remove this once we have a better solution.
_UNSAFE_PYTHON_TOKENS = re.compile('[a-zA-Z0-9_]+|[^a-zA-Z0-9_]+')

# TODO(b/148972318): Remove this once we have a better solution.
_UNSAFE_PYTHON_TOKENS_MAP = {
    'and': 'and_',
    'as': 'as_',
    'assert': 'assert_',
    'break': 'break_',
    'class': 'class_',
    'continue': 'continue_',
   
