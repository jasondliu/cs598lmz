import _struct
import _sys
import sys
import termios
import tty

import _common


@_common.singleton
class console:
    STDIN = 0
    STDOUT = 1
    STDERR = 2

    # deactivate echo only if terminal is a tty
    if _sys.stdout:
        if _sys.stdout.isatty():
            buffer = _sys.stdout.buffer
            if _sys.stdout.buffer is _sys.stdout:
                buffer = sys.stdout.buffer
            dev_tty = _os.ttyname(_os.dup(buffer.fileno())).encode()
            with open(dev_tty, 'rb') as f:
                buffer.fileno()

                old_settings = _termios.tcgetattr(f)
                new_settings = _termios.tcgetattr(f)
                new_settings[3] = (new_settings[3] & ~_termios.ECHO)

            @_common.register_handler(signals.SIGINT)
            def interrupt(*_):
                _
