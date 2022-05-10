import ctypes
ctypes.cast(0, ctypes.py_object).value = 'py'
import subprocess

def call_python(argv):
    """ Call python script without exiting the interpreter.
        Used for debugging. """
    def _get_python_args():
        return [sys.executable, '-u'] + sys.argv[1:]
    # Save current command line, python script and its arguments.
    sys.argv[1:] = argv
    try:
        subprocess.call(_get_python_args())
    except KeyboardInterrupt:
        pass

