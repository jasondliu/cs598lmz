import lzma
lzma_mode = lzma.FORMAT_RAW | lzma.CHECK_CRC32
lzma_preset = 6




class Promise(object):
    def __init__(self, func, *args, **kwargs):
        self._resolved = False
        self._result = None
        self._exception = None
        self._func = func
        self._args = args
        self._kwargs = kwargs
        self._result_callback = None
        self._exception_callback = None

    def __call__(self):
        return self.get()

    def resolve(self):
        if self._resolved:
            return
        try:
            self._result = self._func(*self._args, **self._kwargs)
            self._resolved = True
        except Exception as e:
            self._exception = e
            self._resolved = True
            raise
        if self._result_callback is not None:
            self._result_callback(self._result)
        return self._result

