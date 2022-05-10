import mmap
import os
import re
import sys
import tempfile
import unittest

from functools import wraps

try:
    import cPickle as pickle
except ImportError:
    import pickle

import gevent

from gunicorn.config import Setting, validate_callable
from gunicorn import util

from gunicorn.workers import sync
from gunicorn.workers.sync import SyncWorker

def with_worker(cls):
    @wraps(cls)
    def wrapper(self, *args, **kwargs):
        config = dict()
        config['bind'] = "127.0.0.1:0"
        config['workers'] = 1
        config['backlog'] = 2048
        config['proc_name'] = "test_worker"
        config['worker_class'] = "gunicorn.tests.test_workers.DummyWorker"
        config['worker_connections'] = 10
        config['max_requests'] = 1
        config['max_requests_jitter'] = 0
        config['timeout'] =
