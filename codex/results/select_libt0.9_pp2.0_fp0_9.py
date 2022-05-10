import select
import threading


class AsyncDispatcher:
    """ Uses a thread to asynchronously dispatch incoming messages.  This
        will cause problems in certain situations (like if the onInterface*
        method blocks for too long).  Use SyncDispatcher for a safe-but-slow
        version.
    """
    def __init__(self, parent):
        self._parent = parent
        self._thread = threading.Thread(target = do_dispatch_loop, args = (self,))
        self._protocol = None


    def start(self, protocol):
        assert self._protocol is None
        self._protocol = protocol
        self._thread.start()


    def stop(self):
        # when the thread calls _protocol.close(), it will set self._protocol
        # to None, which will cause it to exit
        self._protocol.close()
        self._thread.join()


    def dispatch(self, data):
        self._parent.onInterfaceDispatch(data)


def do_dispatch_loop(dispatcher):
    """
