import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class test(object):
    def __init__(self):
        self.name = "test"
        self.func = FUNTYPE(self.test)

    def test(self):
        print("Hello %s" % (self.name))

if __name__ == "__main__":
    t = test()
    t.func()
    t.name = "test2"
    t.func()
</code>
This works as expected:
<code>Hello test
Hello test2
</code>
However, if I try to create a list of these functions, I get the following:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class test(object):
    def __init__(self):
        self.name = "test"
        self.func = FUNTYPE(self.test)

    def test(self):
        print("Hello %s" % (self.name))

if __name__ == "__main__":
    t = test()

    l = [t.func, t.func
