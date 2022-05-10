import gc, weakref
import itertools
import json
import logging
import pkgutil
import re
import socket
import traceback
import types
import uuid
import warnings

import numpy as np
import pandas as pd
import pyarrow

from dask.distributed import future as daskFuture
from distributed.client import Future
from distributed.utils_test import cluster, gen_cluster, loop  # noqa: F401
from distributed.utils_test import inc, div, dec, double, add, slowinc  # noqa: F401

from time import time

from .util import test_client_in_process, run_tests

executor_tests = pd.DataFrame(
    columns=["name", "function", "kwargs", "kwargs_descriptor", "data_descriptor"],
)

# Retrieve all executor tests to be run
for _, name, _ in pkgutil.iter_modules([os.path.dirname(__file__)]):
    module = importlib.import_module(f"modin.execution.test.{name
