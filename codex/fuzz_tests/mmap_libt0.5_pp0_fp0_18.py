import mmap
import os
import shutil
import sys
import tempfile
import time
import unittest

from contextlib import contextmanager
from distutils.version import LooseVersion
from functools import partial
from os import path
from subprocess import Popen, PIPE

from mock import patch

from tests.common import (
    assert_command,
    assert_command_success,
    assert_command_failure,
    assert_command_output,
    assert_command_output_json,
)
from tests.common.mock_cluster import MockCluster
from tests.common.skip import SkipIfLocal
from tests.common.test_dimensions import (
    create_exec_option_dimension,
    create_uncompressed_text_dimension,
)
from tests.util.filesystem_utils import WAREHOUSE, IS_S3
from tests.util.hdfs_util import NAMENODE
from tests.util.test_file_parser import QueryTestSectionReader

# IMPALA-2991: Impala's S3 filesystem support is unreliable when running
