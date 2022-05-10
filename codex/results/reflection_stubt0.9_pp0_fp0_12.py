fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
print("should fail")

# second attempt, fails due to check done in implicit context manager
import _codecs, _warnings
_codecs.register_error("fail", lambda x: gi)
_codecs.lookup("fail")("a")
print("should fail")

# third attempt, fails due to __exit__ not being specified
import requests
response = requests.get("http://example.com")
response.__enter__()
print("should fail")

# fourth attempt, fails because it is called before the first
with open("/etc/hostname") as f:
    f.__exit__(0, "", "")
print("should fail")

# fifth attempt, fails because generators cannot be called with positional arguments
f = lambda x: gi
f(0)
print("should fail")

# sixth attempt, works because function calls ignore __init__
class C:
    i = 1

class D(C):
    i = 2

    def __init__(self):
        self.i += 1

d = D
