import socket
import sys
import threading
import time
import traceback

import pytest

from pyspark.sql import SparkSession
from pyspark.sql.utils import AnalysisException
from pyspark.testing.sqlutils import ReusedSQLTestCase, have_pandas, have_pyarrow, \
    pandas_requirement_message, pyarrow_requirement_message, \
    quiet_py4j, ReusedPySparkTestCase


@unittest.skipIf(
    not have_pandas or not have_pyarrow,
    pandas_requirement_message or pyarrow_requirement_message)
class ArrowTests(ReusedSQLTestCase):

    @classmethod
    def setUpClass(cls):
        ReusedSQLTestCase.setUpClass()
        cls.tempdir = tempfile.NamedTemporaryFile(delete=False)
        cls.tempdir.close()

    @classmethod
    def tearDownClass(cls):
        ReusedSQLTestCase.tearDownClass()
