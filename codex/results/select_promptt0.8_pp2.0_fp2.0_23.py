import select
# Test select.select is implemented on Windows.
import socket
with socket.socket() as s:
    select.select([s], [], [])

import pathlib
import sys
import unittest

from mypy.build import (
    BuildSource,
    ParseError,
)
from mypy.errors import CompileError
from mypy.test.helpers import assert_string_arrays_equal
from mypy.test.data import (
    DataDrivenTestCase, DataSuite, DataDrivenTestSuite,
)
from mypy.test.config import test_data_prefix, test_temp_dir
from mypy.test.testtypecheck import is_semantic_error
from mypy.traverser import TraverserVisitor
from mypy.nodes import MypyFile, TypeInfo
from mypy.options import Options
from mypy.types import Type
from mypy import experiments


class BuildTests(DataSuite):
    files = ['build-basic',
             'build-custom-types',
             'build-custom-builtins',
             'build-non
