fn = lambda: None
# Test fn.__code__

def setup_module(mod):
    if verbose: print("setup_module      ", mod.__name__)

def teardown_module(mod):
    if verbose: print("teardown_module   ", mod.__name__)

class TestClass:

    @classmethod
    def setup_class(cls):
        if verbose: print("setup_class       ", cls.__name__)

    @classmethod
    def teardown_class(cls):
        if verbose: print("teardown_class    ", cls.__name__)

    def setup_method(self, method):
        if verbose: print("setup_method      ", method.__name__)

    def teardown_method(self, method):
        if verbose: print("teardown_method   ", method.__name__)

    def test_1(self):
        if verbose: print("test_1")

    def test_2(self):
        if verbose: print("test_2")
