fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = gi.__code__

# ------------------------------------------------------------------------------
# 
# ------------------------------------------------------------------------------

def _is_nested_call(frame):
    return frame.f_back and frame.f_back.f_back and frame.f_back.f_back.f_code == frame.f_code

def _stack_to_frame(stack):
    return stack[0]

def _frame_to_stack(frame):
    return (frame, frame.f_code, frame.f_lineno)


def _frame_to_stack_mock(frame):
    """
    This is used to simulate the behavior of sys._getframe() when the debugger
    is active.
    """
    assert frame.f_back is None
    return (frame, frame.f_code, frame.f_lineno)

def _frame_to_stack_mock_nested(frame):
    """
    This is used to simulate the behavior of sys._getframe() when the debugger
    is active.
    """
    assert frame.f_back is
