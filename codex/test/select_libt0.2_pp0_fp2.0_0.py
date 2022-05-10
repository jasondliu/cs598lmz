import select
import socket
import sys
import threading
import time
import traceback

import pytest

from . import test_utils
from . import utils
from . import vtgate_client
from . import vtgate_utils
from . import vttest_utils
from . import vtworker_utils
from . import zkocc_utils
from . import zktestserver
from . import zkutils

# the default topology for this test
shard_0_master = 'test_nj-0000062346'
shard_1_master = 'test_nj-0000062347'
shard_2_master = 'test_nj-0000062348'
shard_3_master = 'test_nj-0000062349'

shard_0_replica = 'test_nj-0000062350'
shard_1_replica = 'test_nj-0000062351'
shard_2_replica = 'test_nj-0000062352'
shard_3_replica = 'test_nj-0000062353'
