fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
sorted(fn, key=id)

def f():
    pass
f.__call__ = lambda *a, **kw: f
sorted(f, key=id)

'''
print('Theano setup')
import theano
print(theano.__file__)
print(theano.initrd)
print(theano.__version__)
print('===========')

print('Tensorflow setup')
import tensorflow
print(tensorflow.__file__)
print(tensorflow.__version__)
print('===========')
