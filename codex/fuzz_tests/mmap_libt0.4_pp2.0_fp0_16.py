import mmap
import os
import re
import sys
import time
import traceback

from datetime import datetime
from functools import wraps
from io import StringIO
from textwrap import dedent

import pytest

from _pytest.config import ExitCode
from _pytest.compat import _format_args
from _pytest.compat import _format_excinfo
from _pytest.compat import _format_explanation
from _pytest.compat import _format_final_exc_line
from _pytest.compat import _format_tb
from _pytest.compat import _get_fslslash
from _pytest.compat import _get_traceback_frames
from _pytest.compat import _get_traceback_frames_variables
from _pytest.compat import _get_user_encoding
from _pytest.compat import _get_win_unicode_console_len
from _pytest.compat import _is_ascii_encoding
from _pytest.compat import _is_utf8_encoding
