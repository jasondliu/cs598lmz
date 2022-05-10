fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi  # type: ignore

logger = logging.getLogger(__name__)


def get_func_name(func):
    func_name = func if isinstance(func, str) else func.__name__
    if not six.PY2:
        func_name = str(func_name)
    return func_name


def get_console_utf8(s, errors='ignore'):
    if six.PY2:
        return s.encode('utf-8', errors)
    else:
        return s.encode('utf-8', 'namereplace')


def get_traceback_utf8(s, errors='ignore'):
    if six.PY2:
        return s
    else:
        return s.encode('utf-8', errors)


class Tracer(object):
    TRACING_PACKAGES = {'supervisor'}
    TRACING_MODULES = {'supervisor.supervisorctl'}
    TRACING_CLASSES = {}
    TRACING_FUNCTIONS =
