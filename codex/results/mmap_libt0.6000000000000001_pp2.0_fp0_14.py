import mmap
import subprocess
import time
from subprocess import PIPE
from threading import Thread

from tests.helpers.agent import Agent
from tests.helpers.assertions import has_datapoint_with_dim, tcp_socket_open
from tests.helpers.util import ensure_always, run_subprocess, wait_for, wait_until


class Processes(Agent):
    def __init__(self, *args, **kwargs):
        super(Processes, self).__init__(*args, **kwargs)
        self.sleep = None
        self.sleep_pid = None
        self.sleep_proc = None
        self.sleep_proc_exit_code = None
        self.sleep_proc_start_time = None
        self.sleep_proc_stop_time = None
        self.sleep_proc_stop_time_monotonic = None
        self.sleep_proc_stop_time_unix = None
        self.sleep_proc_stop_time_boottime = None

        self.sleep_proc_start_time_monotonic = None
