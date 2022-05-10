import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import pytest

from code.cli.main import main
from code.helper.logger import Logger

l = logging.getLogger("code.tests.cli")
logger = Logger(l)

def test_main_no_args(capsys):
    """
    Tests that main works without arguments
    """

    with pytest.raises(SystemExit) as e:
        main([])

    assert e.value.code == 0
    out, err = capsys.readouterr()
    assert out == ""

def test_main_help(capsys, monkeypatch):
    """
    Tests that main help works
    """

    def mock_exit(a=0):
        pass
    monkeypatch.setattr(sys, "exit", mock_exit)

    main(["-h"])
    out, err = capsys.readouterr()
    assert out.startswith("Usage: code")

@pytest.mark.parametrize("
