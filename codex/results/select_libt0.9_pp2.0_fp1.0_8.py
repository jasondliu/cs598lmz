import selectors


class BaseAsyncEventLoop(object):
    '''
        Refer to the `_select` method of `SocketServer`
        and `socketserver` module
    '''

    def __init__(self, onErr=None, timeout=0.5):
        if not callable(onErr):
            raise TypeError('onErr must be a callable')

        if not isinstance(timeout, numbers.Number) or timeout < 0:
            raise TypeError('invalid timeout: %r' % (timeout,))

        self._onErr = onErr
        self._timeout = timeout

    def _select(self, rlist, wlist, xlist, timeout=None):
        if rlist or wlist or xlist:
            r, w, x = select.select(rlist, wlist, xlist, timeout)
        else:
            r, w, x = [], [], []

        return r, w, x

    def serve_forever(self):
        while True:
            #
            # First we must check and reset the condition.
