import mmap
import os
import re
import subprocess
import sys
import tempfile

from gslib.tests.util import ObjectToURI as suri


def _GetUserAgent(gsutil_api):
  """Returns the user agent string used by the provided gsutil_api instance.

  Args:
    gsutil_api: gsutil Cloud API instance.

  Returns:
    User agent string.
  """
  return gsutil_api.http_wrapper.config.user_agent


def _RunGsUtil(gsutil_api, *args, **kwargs):
  """Runs gsutil command and returns the subprocess instance.

  Args:
    gsutil_api: gsutil Cloud API instance.
    *args: Command line arguments to pass to gsutil.

  Returns:
    Subprocess instance corresponding to gsutil command.
  """
  gsutil_cmd = [sys.executable, gsutil_api.gsutil_bin_path]
  gsutil_cmd.extend(args)
  return subprocess.P
