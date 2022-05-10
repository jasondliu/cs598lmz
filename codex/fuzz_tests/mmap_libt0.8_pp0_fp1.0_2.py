import mmap
import os
from shutil import copyfileobj
from tempfile import NamedTemporaryFile
from unittest.mock import patch

from flask import Flask
import pytest

from songrecsys.server import SongRecSys
from songrecsys.song import AudioFeatures

from .test_server import _mock_flask_run


@pytest.fixture()
def client():
    app = Flask(__name__)
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_version(mocker, client):
    mocker.patch.object(SongRecSys, 'version', return_value='1.2.3')
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'1.2.3' in rv.data


def test_get_available_models(mocker, client):
    mocker.patch.object(SongRecSys, 'available_models', return_value=['model1', 'model2'])

