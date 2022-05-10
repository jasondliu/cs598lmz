import selectors
import shlex
import subprocess
import sys
import time
from typing import Any
from typing import Deque
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from . import _common
from . import agent
from . import auth
from . import proxy


def _read(fd: int) -> bytes:
    data = b""
    while True:
        try:
            buf = os.read(fd, 4096)
        except BlockingIOError:
            break
        if not buf:
            break
        data += buf
    return data


def _write(fd: int, data: bytes) -> None:
    while data:
        try:
            n = os.write(fd, data)
        except BlockingIOError:
            selectors.DefaultSelector().select(timeout=0.1)
            continue
        data = data[n:]


class ExitStatus(Enum):
    SUCCESS = 0
    FAILURE = 1
    TIMEOUT = 2


class Pipe:
    """
