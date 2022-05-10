import _struct
# Test _struct.Struct
import _testcapi
# Test Python API thread state
import sys
import thread
import test.support
from subprocess import Popen, PIPE, STDOUT, check_output

from test.support.script_helper import args_from_interpreter_flags, \
        assert_python_ok, assert_python_failure, spawn_python, kill_python, \
        make_script


def get_type_size(code):
    code = 'import _testcapi; print(_testcapi.get_type_size("{}"))'.format(code)
    return int(check_output([sys.executable, '-c', code]).strip())

def test_python_api():
    # Test _testcapi.with_tp_del
    thread.start_new_thread(
        _testcapi._test_thread_state, (123,))
    thread.start_new_thread(
        _testcapi._test_thread_state, (456,))
    # wait a while before exiting
    time.sleep(0.01)

def
