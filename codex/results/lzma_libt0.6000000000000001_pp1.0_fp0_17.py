import lzma
lzma.LZMAError

import pytest
import redis

from werkzeug.exceptions import BadRequest

from .fixtures import app, client, config
from .fixtures.fakes import FakeRedis
from .fixtures.fakes import FakeStorage
from .fixtures.fakes import FakeContainer
from .fixtures.fakes import FakeBlob
from .fixtures.fakes import FakeBlobData

from .fixtures.fakes import FakeRedisWithPrefix
from .fixtures.fakes import FakeStorageWithPrefix
from .fixtures.fakes import FakeContainerWithPrefix
from .fixtures.fakes import FakeBlobWithPrefix
from .fixtures.fakes import FakeBlobDataWithPrefix

from .fixtures.fakes import FakeRedisWithContainer
from .fixtures.fakes import FakeStorageWithContainer
from .fixtures.fakes import FakeContainerWithContainer
from .fixtures.fakes import FakeBlobWithContainer
from .fixtures.fakes import FakeBlobDataWithContainer

from .fixtures.fakes import Fake
