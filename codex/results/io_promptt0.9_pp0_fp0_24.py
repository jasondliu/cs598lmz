import io
# Test io.RawIOBase instead of io.IOBase to ensure we get read/write/seek
# methods that operate on bytes, not characters.
if hasattr(io, 'RawIOBase'):
    from io import RawIOBase
else:
    from io import BaseRawIO as RawIOBase

from .util import coerce_string_conf
from .handlers import BaseProcessHandler


def start_process(cmd,
                  cwd=None,
                  shell=False,
                  subprocess_flags=None,
                  env=None,
                  stdin=None,
                  stdout=None,
                  stderr=None,
                  wait=True,
                  handler=None,
                  preexec_fn=None,
                  close_fds=False,
                  restore_signals=True,
                  loop=None,
                  logger=None,
                  encoding=None,
                  errors=None,
                  mode=None,
                  text=None,
                  universal_newlines=None):
    """Creates a subprocess and returns a handle to it

    :param cmd:
        The command to run.


