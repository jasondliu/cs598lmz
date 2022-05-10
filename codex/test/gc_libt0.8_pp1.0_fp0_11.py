import gc, weakref

def _get_source_file_path():
    """
    Inspect the stack with Python's 'inspect' module
    and extract the first frame info.
    """
    frame = inspect.currentframe()
    try:
        while True:
            frame = frame.f_back
            if frame.f_code.co_filename != __file__:
                # Windows paths use backslashes, avoid escaping them:
                return frame.f_code.co_filename
    finally:
        del frame


