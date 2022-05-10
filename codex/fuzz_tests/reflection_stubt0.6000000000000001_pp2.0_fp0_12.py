fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

try:
    marshal.dumps(fn)
except TypeError as e:
    print(e)

try:
    marshal.loads(b"cbuiltins\ncode\nq\x00X\x04\x00\x00\x00evalq\x01")
except ValueError as e:
    print(e)
