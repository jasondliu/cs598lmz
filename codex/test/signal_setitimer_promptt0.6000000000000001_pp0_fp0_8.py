import signal
# Test signal.setitimer()
try:
    signal.setitimer(signal.ITIMER_REAL, 0, 0.1)
except:
    print('SKIP')
    raise SystemExit

import uasyncio as asyncio


def cb(signum, frame):
    print('tick!')


loop = asyncio.get_event_loop()
loop.add_signal_handler(signal.SIGALRM, cb)
loop.run_forever()
