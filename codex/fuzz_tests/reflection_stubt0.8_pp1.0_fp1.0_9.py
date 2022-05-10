fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = ()
gi.gi_frame = fn
gi.gi_running = True
gi.gi_code.co_name = 'test'
gi.gi_code.co_filename = '/test.py'
gi.gi_code.co_firstlineno = 1
gi.gi_code.co_code = ()
gi.gi_code.co_consts = ()
gi.gi_code.co_names = ()
gi.gi_code.co_varnames = ()
gi.gi_code.co_cellvars = ()
gi.gi_code.co_freevars = ()
gi.gi_code.co_argcount = 0
gi.gi_code.co_flags = 1048576
gi.gi_frame.f_globals = {}
gi.gi_frame.f_locals = {}

@patch('sys.exc_info')
@patch('sys.stderr')
@patch('logging.StreamHandler')
@patch('logging.getLogger')
def test_log_traceback(*mocks):
