import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import time

from distutils.version import LooseVersion

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.six import iteritems
from ansible.module_utils._text import to_bytes, to_native
from ansible.module_utils.parsing.convert_bool import boolean
from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE
from ansible.module_utils.parsing.convert_bool import BOOLEANS_FALSE

from ansible.module_utils.six.moves import shlex_quote

from ansible.module_utils.urls import fetch_url, url_argument_spec
from ansible.module_utils.six.moves.urllib.parse import urlencode
from ansible.module_utils.six.moves.urllib.parse import urlparse
from ansible.module_utils.six.moves.ur
