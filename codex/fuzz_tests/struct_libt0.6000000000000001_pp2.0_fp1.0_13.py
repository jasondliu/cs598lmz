import _struct
import _sys

def add_error_stream(stream):
    """Add the given stream to the list of streams to which errors are
    written when an exception is raised.
    """
    _sys.__stderr__.add_stream(stream)

def add_output_stream(stream):
    """Add the given stream to the list of streams to which output is
    written when a print statement is executed.
    """
    _sys.__stdout__.add_stream(stream)

def add_warning_stream(stream):
    """Add the given stream to the list of streams to which warnings are
    written when a warning is raised.
    """
    _sys.__stderr__.add_stream(stream)

def get_error_streams():
    """Return the list of streams to which errors are written when an
    exception is raised.
    """
    return _sys.__stderr__.get_streams()

def get_output_streams():
    """Return the list of streams to which output is written when a
    print statement is executed.
