import _struct
# Test _struct.Struct.__reduce__
import pickle

class S(object):
    def __reduce__(self):
        return (S, ())

s = S()

for fmt in ('i', 'ii', 'iii'):
    st = _struct.Struct(fmt)
    st2 = pickle.loads(pickle.dumps(st))
    assert st.format == st2.format

print('ok')
