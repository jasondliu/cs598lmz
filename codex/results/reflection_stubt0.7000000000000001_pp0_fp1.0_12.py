fn = lambda: None
gi = (i for i in ())
fn.__code__ = (ui, ki, ci, coi, abi, si, nci, ki, ci, gi,
               ci, O, O, O, O, O, O, O, O, O, O, O, O, O)
fn.__closure__ = (gi.gi_frame,)

def test_async_function():
    fn.__code__ = (ui, ki, ci, coi, abi, si, nci, ki, ci, gi,
                   ci, O, O, O, O, O, O, O, O, O, O, O, O, O)
    fn.__closure__ = (gi.gi_frame,)
    assert inspect.iscoroutinefunction(fn)

def test_not_async_function():
    fn.__code__ = (ui, ki, ci, coi, si, nci, ki, ci, gi,
                   ci, O, O, O, O, O, O, O, O, O, O, O, O, O)
    fn.__
