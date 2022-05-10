fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()

# Should not crash
try:
    fn.__code__ = 1
except TypeError:
    pass

# Should not crash
try:
    fn.__code__()
except TypeError:
    pass

# Should not crash
try:
    fn.__code__ = None
except TypeError:
    pass

# Should not crash
try:
    fn.__code__()
except TypeError:
    pass

# Should not crash
try:
    fn.__code__ = lambda: None
except TypeError:
    pass

# Should not crash
try:
    fn.__code__()
except TypeError:
    pass

# Should not crash
try:
    fn.__code__ = gi
except TypeError:
    pass

# Should not crash
try:
    fn.__code__()
except TypeError:
    pass

# Should not crash
try:
    fn.__code__ = 1
except TypeError:
    pass

# Should not crash
try:
    fn.
