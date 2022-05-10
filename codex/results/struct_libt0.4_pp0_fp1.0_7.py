import _struct
import pyclbr
import sys
import time

class _Test(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.result = None

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start = time.time()
            try:
                self.result = func(*self.args, **self.kwargs)
            except Exception as e:
                self.result = e
            finally:
                self.elapsed = time.time() - start
        return wrapper

def _run_tests(module, test_class):
    tests = []
    for name, obj in pyclbr.readmodule(module).items():
        if isinstance(obj, pyclbr.Class):
            if obj.name == test_class:
                for name, obj in obj.methods.items():
                    if name.startswith('test_'):
                        tests.append(getattr(module, name))
    for test in tests:
