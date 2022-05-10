fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
gi.gi_code = fn.__code__
gi.gi_frame = fn.__code__
gi.gi_running = fn.__code__
fn.gi_code = gi
fn.gi_frame = gi
fn.gi_running = gi


def raise_helper(type, value, traceback):
    """Helper function for raising."""
    if traceback is None:
        return type(value)
    elif isinstance(traceback, tuple):
        return type(value).with_traceback(traceback[0])
    else:
        return type(value).with_traceback(traceback)


class UnexpectedFrameStart(Exception):
    """Exception that is thrown if a frame starts unexpectedly."""

def _find_frame_end(fp):
    """Find the end of a frame."""
    token = fp.readline()
    if not token:
        raise EOFError
    if token.strip() != FRAME_START:
        raise UnexpectedFrameStart(
            "Expected frame start token not found, got
