import threading
threading.stack_size(1 << 25)  # Increase stack size to avoid stack overflow while

import sys
sys.setrecursionlimit(10 ** 6)  # Max recursion depth for python

FINISHED, READY, RUNNING, BLOCKED, REJECTED, EXIT = 1, 2, 3, 4, 5, 6


class Process:
    def __init__(self, pid, state, need, available, max, allocation):
        self.pid = pid
        self.state = state
        self.need = need
        self.available = available
        self.max = max
        self.allocation = allocation


class BrokenProcess(BaseException):
    pass


def can_request(process, resources, available_resources):
    if all([x <= y for x, y in zip(resources, process.need)]):
        return all([x <= y for x, y in zip(resources, available_resources)])
    else:
        return False


def can_release(process, resources, available_resources):
    if all([x <= y for x, y in zip(
