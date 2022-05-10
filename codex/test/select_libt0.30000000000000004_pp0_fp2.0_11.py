import select
import socket
import sys
import threading
import time
import traceback

import pytest

import pytest_asyncio
from pytest_asyncio import compat
from pytest_asyncio import constants
from pytest_asyncio import exceptions
from pytest_asyncio import utils


class TestAsyncioEventLoop(object):

    @pytest.fixture
    def event_loop(self, event_loop_factory):
        return event_loop_factory()

    def test_event_loop_factory(self, event_loop_factory):
        assert event_loop_factory() is event_loop_factory()

    def test_event_loop_factory_with_policy(self, event_loop_factory):
        event_loop_factory(policy=compat.TestSelector())
