import select
import socket
import sys
import threading
import time

import pytest

from aiohttp import web
from aiohttp.test_utils import make_mocked_coro, make_mocked_request
from aiohttp.web import (
    Application,
    Request,
    Response,
    StreamResponse,
    WebSocketResponse,
    WSMsgType,
    run_app,
    run_app_threaded,
    run_app_processes,
    run_app_in_thread,
    run_app_in_subprocess,
    _run_app,
    _run_app_threaded,
    _run_app_processes,
    _run_app_in_thread,
    _run_app_in_subprocess,
    _AppRunner,
    _AppRunnerBase,
    _AppRunnerThreaded,
    _AppRunnerProcesses,
    _AppRunnerInThread,
    _AppRunnerInSubprocess,
)
from aiohttp.web_runner import _set_signals_handler
