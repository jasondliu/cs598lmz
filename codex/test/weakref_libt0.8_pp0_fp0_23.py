import weakref
from .utils import Process, socket


class AppMgr(object):
    def __init__(self, app):
        self.app = app
        self.apps = {}  # process_idx: app_obj
        self.ev_loop = None
        self.ev = None

    def start(self, loop=None, ev=None):
        if loop is None:
            loop = asyncio.get_event_loop()
            self.ev_loop = loop
        if ev is None:
            ev = get_loop_async_event(loop)
            self.ev = ev

        # keep the same loop in all coros in this process
        self.app.loop = loop
        self.app.ev = ev
        self.app.mgr_init()
        # start the app
        loop.run_until_complete(asyncio.gather(self.app.start(), loop=loop))
        loop.run_forever()

    def stop(self):
        if self.ev_loop is not None:
            self.ev_loop.stop()
