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
from _pytest.assertion.util import (
    _get_previous_assertion_error,
    _format_assertmsg,
    _format_explanation,
    _format_explanation_of_assertion_error,
    _format_assertion_message,
    _format_assertion_message_with_explicit_message,
    _format_assertion_message_without_explicit_message,
    _format_assertion_message_with_diff,
    _format_assertion_message_without_diff,
    _format_assertion_message_with_diff_and_explicit_message,
    _format_assertion_message_without_diff_and_explicit_message,
    _
