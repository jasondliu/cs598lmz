import sys, threading

def run():
    import asyncio
    async def pause(interval):
        loop = asyncio.get_event_loop()
        await asyncio.sleep(interval)

    @asyncio.coroutine
    def async_queue_task(*args, **kwargs):
        import asyncqueue
        def callback(result):
            print("callback:", result)
        while True:
            handle = q.get()
            try:
                print("start:", handle)
                val = yield from handle
                print("done: ", val)
            except Exception as e:
                print("failure: ", e)
            else:
                callback(val)
            finally:
                pass

    import pyuv
    loop = pyuv.Loop.default_loop()
    q = asyncqueue.AsyncQueue(loop, async_queue_task)

    # h = asyncio.wait_for(pause(1), 1, loop=loop)
    # q.put(h)

    q.put(loop.create_timer())

    loop.run()

def main():
    sys.setrecursion
