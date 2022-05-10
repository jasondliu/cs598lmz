import select
import signal
import threading
import time

from .perfclient import PerfClient
from .perfstats import PerfStats


class Perf(object):
    """Interface for interacting with the perf linux tool.

    Because perf is a command-line tool that has many different options, this
    interface may not cover every possible use case. However, it should cover
    the common use cases.

    If you do encounter a case where the perf tool is not being used as you
    expect, please file a bug at http://crbug.com/new.

    The perf tool has some performance overhead, so the recommended way to use
    the tool is to run it for a short time, dump the data to perf.data, and then
    examine that perf.data file. The PerfStat and PerfClient interfaces exist to
    help with this workflow.
    """

    @staticmethod
    def check_call(cmd, **kwargs):
        """Execute a command as a child process, raising any errors.

        This is a static method because it is intended to serve as a drop-in
        replacement for subprocess.
