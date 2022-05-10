fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# The following should not be caught by the exception handler
try:
    raise Exception
except:
    pass

# The following should not be caught by the exception handler
try:
    raise Exception
except Exception:
    pass

# The following should not be caught by the exception handler
try:
    raise Exception
except Exception as e:
    pass

# The following should not be caught by the exception handler
try:
    raise Exception
except Exception as e:
    raise e

# The following should not be caught by the exception handler
try:
    raise Exception
except Exception as e:
    raise e from None

# The following should not be caught by the exception handler
try:
    raise Exception
except Exception as e:
    raise e from Exception

# The following should not be caught by the exception handler
try:
    raise Exception
except Exception as e:
    raise e from Exception()

# The following should not be caught by the exception handler
try:
    raise Exception
except Exception as e:
    raise e from Exception() as e2:
    pass

