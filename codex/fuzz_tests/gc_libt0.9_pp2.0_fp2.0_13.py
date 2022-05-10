import gc, weakref
import warnings
import argparse
import functools
import itertools

SNOOP = 10
DDD = 24
CACHE = 0

colorama.init()

class AsyncContextManager(object):
    def __init__(self):
        self._lock = asyncio.Lock()

    async def __aenter__(self):
        await self._lock.acquire()

    async def __aexit__(self, *args):
        self._lock.release()


class Turn:
    def __init__(self, args):
        self.wait = asyncio.Event()
        self.sem = asyncio.Semaphore(args.threads)
        self.args = args

    async def __aenter__(self):
        await self.sem.acquire()
        if self.args.debug == DDD:
            print(colorama.Fore.GREEN + "turn >" + colorama.Style.RESET_ALL)

    async def __aexit__(self, *args):
        if self.args.debug == DDD:
            print
