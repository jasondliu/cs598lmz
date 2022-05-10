import mmap
import os
import pytest
import re
import sqlite3

from chaossystemd import meta


class Custom_data(object):

    def __init__(self, name, value):
        self.value = value
        self.name = name
        self.start_time = None
        self.end_time = None
        self.duration_seconds = None
        self.duration_microseconds = None
        self.invocation_id = None
        self.starting = None
        self.retcode = None


class TestMeta(object):

    @pytest.fixture
    def meta_db(self):
        m = meta.Meta()
        return m

    @pytest.fixture
    def mock_date(self):
        date = datetime.datetime.now()
        return date

    def test_store_metadata(self, meta_db, mock_date, monkeypatch):
        monkeypatch.setattr(meta, 'get_results_dir', lambda: os.getcwd())
        meta_db.store_metadata(mock_date, mock
