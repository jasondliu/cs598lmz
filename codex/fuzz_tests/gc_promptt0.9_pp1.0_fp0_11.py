import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable():

class TestBase:
    def __init__(self):
       self.message = "A class called TestBase"

test = TestBase()
test = None
class TestBase:
    def __init__(self):
       self.message = "A class called TestBase"

test = TestBase()
test = TestBase()
test = TestBase()
test = TestBase()
test = None
# class TestChild(TestBase):
#     def __init__(self):
#        self.message = "A class called TestChild"
#
#
# test = TestChild()
# test = None
# # Test output from __del__ methods:
#
# class test:
#     def __del__(self):
#         print "my __del__ method got called"
#
# test = test()
# test = None
# class test:
#     def __del__(self):
#         print "my __del__ method got called"
#
# test = test()
# test()
# import numpy
# numpy.__version__
#
