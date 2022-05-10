fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
crash_python()

# ____________________________________________________________

def crash_python2():
    # crash Python
    # this one is a bit tricky: it uses the fact that the first argument
    # is a pointer to the frame, and that in PyEval_EvalCodeEx() the
    # frame pointer is used before it is checked for NULL
    fn = lambda: None
    gi = (i for i in ())
    fn.__code__ = gi
    fn()
    crash_python()

def crash_python3():
    # crash Python
    # this one is a bit tricky: it uses the fact that the first argument
    # is a pointer to the frame, and that in PyEval_EvalCodeEx() the
    # frame pointer is used before it is checked for NULL
    fn = lambda: None
    gi = (i for i in ())
    fn.__code__ = gi
    fn()
    crash_python2()

def crash_python4():
    # crash Python
    # this one is a bit tricky: it uses the
