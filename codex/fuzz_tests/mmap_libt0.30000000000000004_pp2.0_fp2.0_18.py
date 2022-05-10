import mmap
import os
import re
import shutil
import sys
import tempfile
import time
import unittest

from six.moves import urllib

from tests import test_utils
from tests.test_utils import (
    TEST_DATA_DIR,
    TEST_WORKING_DIR,
    get_testdata_dir,
    get_test_config,
    get_test_locale,
    get_test_output_dir,
    get_test_src_dir,
    is_in_travis,
    skip_if_env_not_set,
    skip_if_not_python3,
    skip_if_on_windows,
    skip_if_on_travis,
    skip_if_on_appveyor,
    skip_if_on_azure,
    skip_if_on_gitlab,
    skip_if_on_gitlab_ci,
    skip_if_on_travis_or_appveyor,
    skip_if_on_travis_or_azure,
    skip_if_
