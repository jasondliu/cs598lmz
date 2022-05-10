fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ is not a code object
def fa(m=__code__): (__code__)
fa()

# __code__ is not a code object
def fa(m=__code__): (__code__)
fa(__code__)

# __traceback__ is only valid in an exception handler
def fb(m=__traceback__): (__traceback__)
fb()

# __traceback__ is only valid in an exception handler
def fb(m=__traceback__): (__traceback__)
fb(__traceback__)

# __func__ is not a function
def fc(m=__func__): (__func__)
fc()

# __func__ is not a function
def fc(m=__func__): (__func__)
fc(__func__)

# __closure__ is not valid (yet)
def fd(m=__closure__): (__closure__)
fd()

# __closure__ is not valid (yet)
def fd(m=__
