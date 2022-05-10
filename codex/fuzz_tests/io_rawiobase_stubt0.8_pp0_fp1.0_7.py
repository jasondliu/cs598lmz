import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        self.file = file
        super(File, self).__init__(*args, **kwargs)
    def readinto(self, b):
        n = self.file.readinto(b)
        return n
class RemainingFile(File):
    def __init__(self, file, remaining, *args, **kwargs):
        self.remaining = remaining
        super(RemainingFile, self).__init__(
            file, *args, **kwargs)
    def readinto(self, b):
        if len(b) > self.remaining:
            b = memoryview(b)[0:self.remaining]
        n = self.file.readinto(b)
        if n > self.remaining:
            raise IOError("requested %d bytes but %d bytes remaining"%(
                n, self.remaining))
        self.remaining -= n
        return n

@implementer(ISubscription)
class Subscription(object):
    def __init
