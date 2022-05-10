import select
import socket
import sys
import threading
import time

import pytest

from pyspark.sql.utils import AnalysisException
from pyspark.sql import SparkSession, Row
from pyspark.sql.streaming import StreamingQueryException
from pyspark.sql.types import *
from pyspark.testing.sqlutils import ReusedSQLTestCase, have_pandas, have_pyarrow, pandas_requirement_message, \
    pyarrow_requirement_message, quiet_py4j

if sys.version_info[:2] <= (2, 6):
    try:
        import unittest2 as unittest
    except ImportError:
        sys.stderr.write('Please install unittest2 to test with Python 2.6 or earlier')
