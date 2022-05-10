import mmap
import os
import re
import shutil
import subprocess
import tempfile

from ansible import constants as C
from ansible.errors import AnsibleError, AnsibleFileNotFound
from ansible.module_utils.six import PY3, text_type
from ansible.module_utils._text import to_bytes, to_text
from ansible.module_utils.six import iteritems
from ansible.module_utils.six.moves import shlex_quote
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display

display = Display()

# Try to detect the encoding of a file
#
# This is a modified version of the `chardetect` module, which is
# licensed under the LGPL v2.1. The original copyright notice can be
# found below.
#
# Copyright (C) 2001-2013, Mandriva
#
# Author: Mandriva Linux
#
#  Alexandre Oliveira <aleprj@mandriva.com>
#
