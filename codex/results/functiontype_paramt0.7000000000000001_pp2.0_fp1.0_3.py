from types import FunctionType
list(FunctionType(sorted, 'abc', 'def', lambda x: x))

import pickle
pickle.loads(b'\x80\x03cbuiltins\nstr\nq\x00X\x01\x00\x00\x00AS\x86q\x01\x86q\x02\x87q\x03Rq\x04.')
pickle.dumps(b'a')
pickle.loads(b"c__builtin__\nset\np0\n((lp1\nS'abc'\np2\naS'abc'\np3\naS'abc'\np4\natp5\nRp6\n.")
