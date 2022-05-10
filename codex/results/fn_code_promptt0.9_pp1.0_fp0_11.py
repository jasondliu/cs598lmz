fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__ = lambda: None
fn.__code__.co_argcount = {}
# Test fn.__defaults__
fn.__defaults__ = []
fn.__defaults__[:] = [(lambda: None)]
# Test fn.__defaults__.__len__
fn.__defaults__.__len__ = lambda: 1
# Test fn.__defaults__[0]
fn.__defaults__[0] = {}
fn.__defaults__[0]()
del fn.__defaults__[0]
fn.__defaults__[0] = {}
# Test fn()
fn()
import numpy
# Test numpy.int64.__index__
numpy.int64.__index__ = lambda self: 0
# Test numpy.int64().__index__
numpy.int64().__index__()
# Test numpy.int64.__add__
numpy.int64.__add__ = lambda a, b: 0
# Test numpy.int64().__add__
numpy.int
