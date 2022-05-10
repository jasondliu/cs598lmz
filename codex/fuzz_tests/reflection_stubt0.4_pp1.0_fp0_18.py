fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# __code__ is not a code object
try:
    fn()
except TypeError as e:
    print(e)

# __code__ is not a code object
try:
    fn.__code__.co_code
except AttributeError as e:
    print(e)

# __code__ is not a code object
try:
    fn.__code__.co_filename
except AttributeError as e:
    print(e)

# __code__ is not a code object
try:
    fn.__code__.co_firstlineno
except AttributeError as e:
    print(e)

# __code__ is not a code object
try:
    fn.__code__.co_name
except AttributeError as e:
    print(e)

# __code__ is not a code object
try:
    fn.__code__.co_varnames
except AttributeError as e:
    print(e)

# __code__ is not a code object
try:
    fn.__code__.co
