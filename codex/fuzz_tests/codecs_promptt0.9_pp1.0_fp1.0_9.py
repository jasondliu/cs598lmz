import codecs
# Test codecs.register_error()
CAN_REGISTER_ERRORS = True
try:
    codecs.register_error
except AttributeError:
    CAN_REGISTER_ERRORS = False
CAN_REGISTER_CAPTURE_ERRORS = CAN_REGISTER_ERRORS and not sys.platform.startswith('java')
# Test sys.settrace() in restricted execution mode
# XXX Remove when we do not need to run test_subprocess in restricted
# execution mode anymore)
import _testcapi
CAN_SET_SUBPROCESS_TRACE = _testcapi.get_subprocess_settrace_can_raise()
_testcapi.set_subprocess_settrace_can_raise(False)
try:
    subprocess.call([sys.executable, "-c", "1"],
                    close_fds=True,
                    # subprocess sends the trace function a SIGINT
                    # when it exits, so the process cannot terminate
                    # reliably when a trace function is set;
                    # therefore temporary_dir=None
                    env={"PYTHONPATH": TEST_HOME, "PY
