fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that code objects can't be created from other types of objects.
try:
    def fn(code):
        fn.__code__ = code
    fn(0)
except TypeError:
    print("TypeError")

try:
    def fn(code):
        fn.__code__ = code
    fn(None)
except TypeError:
    print("TypeError")

try:
    def fn(code):
        fn.__code__ = code
    fn(lambda: None)
except TypeError:
    print("TypeError")

try:
    def fn(code):
        fn.__code__ = code
    fn(fn)
except TypeError:
    print("TypeError")

try:
    def fn(code):
        fn.__code__ = code
    fn("")
except TypeError:
    print("TypeError")

try:
    def fn(code):
        fn.__code__ = code
    fn(())
except TypeError:
    print("TypeError")

try:
   
