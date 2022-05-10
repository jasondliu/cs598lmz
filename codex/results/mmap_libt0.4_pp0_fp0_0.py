import mmap
import os
import re
import subprocess
import sys
import tempfile
import time
import traceback

import pytest

from pytest_cov.embed import MultiprocessingData
from pytest_cov.embed import MultiprocessingTracer
from pytest_cov.embed import MultiprocessingTracerPool
from pytest_cov.embed import MultiprocessingTracerPoolManager


def _get_multiprocessing_tracer_pool_manager(tracer_class, tracer_args):
    """
    Return a MultiprocessingTracerPoolManager instance.

    :param tracer_class: A subclass of MultiprocessingTracer.
    :param tracer_args: A tuple of arguments to pass to the tracer class.
    """
    return MultiprocessingTracerPoolManager(
        tracer_class=tracer_class,
        tracer_args=tracer_args,
        max_workers=1,
        multiprocessing_method=None,
    )


class TestMult
