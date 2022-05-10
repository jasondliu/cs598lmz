import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello world\n')).start()

from concurrent.futures import ProcessPoolExecutor
from functools import partial
from multiprocessing import Value
from os import lock, kill, getpid, setpid
from threading import BoundedSemaphore


from contextlib import ExitStack, contextmanager
from itertools import chain
from time import sleep
import multiprocessing


contextmanager def all(*contexts):
    with ExitStack() as stack:
        yield tuple(stack.enter_context(c) for c in contexts)


def do(x, y):
    sleep((x % 3 + 1) / 10)
    return x, y


def f(n, x):
    ns = list(map(lambda pid: Process(pid), range(n)))
    with Pipe(duplex=True) as (r, w):
        loop = get_event_loop()
        future = asyncio.Future()
        loop.add_reader(r, lambda: future.set_result(r.read()))
        loop.call_later(0
