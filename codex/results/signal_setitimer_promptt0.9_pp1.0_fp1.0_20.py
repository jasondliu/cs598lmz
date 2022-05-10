import signal
# Test signal.setitimer() which is only supported on the Linux kernel
# and might raise a RuntimeError on other platforms
supports_setitimer = hasattr(signal, 'setitimer')

from decorator import decorator
from flup.server.fcgi_fork import WSGIServer

from pulsar import send, get_actor, send_robust
from pulsar.apps.greenio import GreenTask
from pulsar.utils import isasync, asynconerror, GreenPipe
from pulsar.apps.wsgi import LazyWsgi, WsgiHandler, HttpRequestHandler
from pulsar.utils.modules import import_module
from pulsar.utils.system import platform
from pulsar.utils.pep import to_bytes, to_string, is_py3, pickle
from pulsar.utils.pep import iscoroutinefunction
from pulsar.utils.greenio import PipeWriter, PipeReader

from .bench import BenchServer
from .util import ping
from .run import RunServer, TestServer
from .multiprocessing import TestClient


sep = to_bytes('\r
