import lzma
lzma.LZMAError

import os
import sys
import time
import shutil
import subprocess
import tempfile
import threading
import traceback
import zipfile

import pytest

import py

from _pytest.assertion import util
from _pytest.assertion.rewrite import AssertionRewritingHook
from _pytest.assertion.util import _get_assertion_module
from _pytest.compat import get_real_func
from _pytest.config import hookimpl
from _pytest.config.argparsing import Parser
from _pytest.config.argparsing import ParserError
from _pytest.config.argparsing import _ensure_value
from _pytest.config.argparsing import _get_parser
from _pytest.config.argparsing import _preparse
from _pytest.config.argparsing import _set_option
from _pytest.config.argparsing import _set_session_config
from _pytest.config.argparsing import _set
