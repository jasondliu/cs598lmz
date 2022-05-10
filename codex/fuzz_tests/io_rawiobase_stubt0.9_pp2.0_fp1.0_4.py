import io
class File(io.RawIOBase):
    def __init__(self, *args):
        pass
    def __enter__(self):
        return self
    def __exit__(self, *args):
        pass
import sys
stdout = File()

def iterator_wrapper(func, *args):
    class EOF:
        pass
    class Iter:
        def __init__(self, *args):
            self.__dict__.update(func(*args))
        def __iter__(self):
            return self
        def __next__(self):
            if self.__iter in self.__dict__:
                self.__dict__.update(self.__iter.__next__())
            if self.__state == -1:
                raise StopIteration()
            if self.__state == 0:
                return EOF
            if self.__state == 1:
                return self.__result
        def __aenter__(self):
            return self
        def __aexit__(self, *args):
            pass
    return Iter(*args)

def iterator_wrapper_a(func
