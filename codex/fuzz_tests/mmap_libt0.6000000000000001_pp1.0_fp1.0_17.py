import mmap
import re
import time

try:
    import cPickle as pickle
except:
    import pickle

try:
    import ujson as json
except:
    import json

import pytest

import pyaem


# TODO: add more tests for resource type
# TODO: add tests for ACLs


@pytest.fixture
def aem_mock():
    aem_mock = pyaem.PyAem(
        'localhost',
        4502,
        'admin',
        'admin',
        'http://localhost:4502/crx/packmgr/service/.json'
    )
    return aem_mock


@pytest.fixture
def aem_mock_https():
    aem_mock = pyaem.PyAem(
        'localhost',
        4503,
        'admin',
        'admin',
        'https://localhost:4503/crx/packmgr/service/.json'
    )
    return aem_mock


@pytest.f
