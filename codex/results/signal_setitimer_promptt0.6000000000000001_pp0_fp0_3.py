import signal
# Test signal.setitimer
#pylint: disable=no-member
signal.setitimer(signal.ITIMER_REAL, 1, 0.5)

import pytest
import threading

from .util import get_port, check_port_is_open, check_port_is_closed, check_port_is_not_open

from nng import Protocols
from nng import Socket


def test_listen_start_stop():
    port = get_port()
    with Socket(Protocols.REP0) as sock:
        sock.listen(f"tcp://127.0.0.1:{port}", 1)
        check_port_is_open(port)
        sock.close()
        check_port_is_closed(port)
        with pytest.raises(RuntimeError):
            sock.listen(f"tcp://127.0.0.1:{port}")
        check_port_is_closed(port)


def test_listen_with_options():
    port = get_port()
    with Socket(Prot
