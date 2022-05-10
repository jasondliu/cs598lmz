import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Threading\n')).start()

import multiprocessing
multiprocessing.Process(target=lambda: sys.stdout.write('Multiprocessing\n')).start()

import asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.ensure_future(loop.run_in_executor(None, lambda: sys.stdout.write('Asyncio\n'))))
loop.close()

import gevent
gevent.spawn(lambda: sys.stdout.write('Gevent\n'))
gevent.wait()

# import twisted
# from twisted.internet import reactor
# from twisted.internet.threads import deferToThread
# reactor.callInThread(lambda: sys.stdout.write('Twisted\n'))
# reactor.run()

import curio
curio.run(curio.spawn(lambda: sys.stdout.write('Curio\n')))

import trio
