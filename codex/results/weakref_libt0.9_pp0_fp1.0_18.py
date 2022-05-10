import weakref
import traceback
from difflib import SequenceMatcher
import sys

# this is a very hacky way to get around the folder directory tree problem
# be sure to add it to the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from flask import request, jsonify
from werkzeug.exceptions import NotFound, BadRequest, Conflict
import pytest

from app import api, create_app


@pytest.fixture
def app():
    app = create_app('config.TestingConfig')
    with app.app_context():
        api.init_app(app)
    yield app

@pytest.fixture
def client(app):
    client = app.test_client()
    yield client

class Event(object):
    """A simple class to approximate the ``blinker.Signal`` API.

    It also allows tracing which events have been attached to, allowing for
