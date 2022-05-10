import socket
socket.if_indextoname(3)

# ---------------
# If a test causes a warning, catch the warning
# ---------------
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    # this is where the test is
    self.assertTrue(True)

# ---------------
# If a test causes a warning, ignore the warning
# ---------------
def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()

# ---------------
# If a test causes a warning, raise the warning
# ---------------
def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("error")
    fxn()

# ---------------
# If a test causes a warning, raise the warning
# ---------------
def fxn():
    warnings.warn("deprecated", DeprecationWarning)
    print "blah"

with warnings.catch_warnings():
    warnings.simplefilter
