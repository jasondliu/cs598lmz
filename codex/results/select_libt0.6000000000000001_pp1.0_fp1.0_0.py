import select
import signal
import sys
import time
from uuid import uuid1

import pytest

from pymemcache.client.base import Client
from pymemcache.exceptions import MemcacheConnectionError, MemcacheUnknownCommandError, MemcacheServerError
from pymemcache.test.utils import MockSocket
from pymemcache.test.utils import get_mock_socket, get_mock_socket_and_client
from pymemcache.test.utils import MockSocketWithFileObject


def test_get_set_delete_cas(mock_server):
    client = Client(('localhost', 11211))

    result = client.set('foo', 'bar')
    assert result is True

    result = client.get('foo')
    assert result == b'bar'

    result = client.get('baz')
    assert result is None

    result = client.set('foo', 'baz')
    assert result is True

    result = client.get('foo')
    assert result == b'baz'

    result = client.delete('foo')
    assert
