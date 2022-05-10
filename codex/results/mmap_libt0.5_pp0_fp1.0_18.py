import mmap
import os
import pathlib
import sys
import tempfile
import unittest

from test import support
from test.support import script_helper


def _write_script(script_dir, script_basename, script_text):
    script_filename = os.path.join(script_dir, script_basename)
    with open(script_filename, "w", encoding="utf-8") as script:
        script.write(script_text)
    return script_filename


def _make_test_script(script_basename, script_text, *, tmp_dir=None):
    script_dir = tempfile.mkdtemp(dir=tmp_dir)
    try:
        script_filename = _write_script(script_dir, script_basename, script_text)
        return script_filename
    except:
        shutil.rmtree(script_dir)
        raise


class _FakeWindowsError(OSError):
    pass


class _FakeWindowsErrorNoFile(OSError):
    pass


class _FakeWindowsErrorFileExists(
