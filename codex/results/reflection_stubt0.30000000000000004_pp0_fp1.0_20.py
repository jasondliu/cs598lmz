fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__dict__ = {'attr': 'value'}
fn.__defaults__ = (1, 2, 3)
fn.__closure__ = (1,)
fn.__globals__ = {'global': 'value'}
fn.__module__ = 'module'

# pickle
import pickle

pickle.dumps(fn)

# marshal
import marshal

marshal.dumps(fn.__code__)

# copyreg
import copyreg

copyreg.pickle(type(fn), lambda fn: (fn.__name__, fn.__code__, fn.__dict__))

# types
import types

types.FunctionType(fn.__code__, fn.__globals__, fn.__name__, fn.__defaults__, fn.__closure__)

# inspect
import inspect

inspect.signature(fn)

# dis
import dis

dis.dis
