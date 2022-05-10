import io
class File(io.RawIOBase):
    """A file-like object that produces a deferred."""
    def __init__(self, producer, *args):
        self._producer = producer
        self._args = args
        self.closed = False
        self._deferred = defer.Deferred()
        self._deferred.addCallback(lambda _: self.close())
        self._producer.registerProducer(self, True)

    def read(self, size=-1):
        if self.closed:
            return b""
        if size < 0:
            return self._deferred
        else:
            return self._deferred.addCallback(lambda data: data[:size])

    def write(self, data):
        return self._deferred.addCallback(lambda _: data)

    def close(self):
        self.closed = True
        self._producer.unregisterProducer()

    def resumeProducing(self):
        d, self._deferred = self._deferred, defer.Deferred()
        d.callback(self._producer.more(*self._args))

class Producer(object
