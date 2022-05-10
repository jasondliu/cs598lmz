import signal
# Test signal.setitimer and signal.getitimer for itimer_virtual and
# itimer_prof.
from test.support import run_with_locale
from time import sleep
from subprocess import Popen, PIPE
abort_called = False

def handler(signum, frame):
    global abort_called
    print('handler called')
    abort_called = True
    raise SystemExit


def test_itimer():
    global abort_called
    if hasattr(signal, 'setitimer'):
        result = Popen([sys.executable, '-c', 'import signal; print(signal.setitimer(signal.ITIMER_VIRTUAL, 2.3, 2.3))'], stdout=PIPE)
        stdout, stderr = result.communicate()
        rc = result.wait()
        if rc:
            print('subprocess failed:', rc)
            print(stdout)
            print(stderr)
        else:
            got = float(stdout)
            print('subprocess ok, set %f' % got)
