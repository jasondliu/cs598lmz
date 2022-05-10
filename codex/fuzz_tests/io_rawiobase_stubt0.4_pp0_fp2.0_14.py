import io
class File(io.RawIOBase):
    def __init__(self, path, mode, *args, **kwargs):
        self.path = path
        self.mode = mode
        self.args = args
        self.kwargs = kwargs
        self.f = None
    def open(self):
        self.f = open(self.path, self.mode, *self.args, **self.kwargs)
    def close(self):
        if self.f:
            self.f.close()
            self.f = None
    def __getattr__(self, name):
        if self.f is None:
            self.open()
        return getattr(self.f, name)
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, *args):
        self.close()
    def __del__(self):
        self.close()

#/home/tianyiz/miniconda3/envs/pytorch_py3.6/lib/python3.6/site-packages/torchvision/dat
