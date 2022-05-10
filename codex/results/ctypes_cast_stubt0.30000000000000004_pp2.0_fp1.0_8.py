import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a hack, but it lets us access the above line as a string.
import io, contextlib, tokenize
with contextlib.redirect_stdout(io.StringIO()) as str_output:
    exec(tokenize.untokenize(tokenize.generate_tokens(iter([line]).__next__)).rstrip())
code = str_output.getvalue()

# Execute the code in a namespace and support tracing utilities by setting a value for frame and tb.
namespace = dict(__name__='__main__', __file__='<stdin>', __builtins__=builtins)
try:
    exec(code, namespace, namespace)
except:
    pass

# Construct the traceback and return it.
import traceback
return traceback.extract_stack(namespace['tb'])
"""

def get_traceback(tb):
    """
    Given a traceback (or exception) in some other process, return the equivalent traceback in this
    process.
    """

   
