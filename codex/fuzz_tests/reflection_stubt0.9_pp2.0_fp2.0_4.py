fn = lambda: None
gi = (i for i in ())
fn.__code__ = 'foo'.encode()
import pickle
cPickle.loads(pickle.dumps(fn))
