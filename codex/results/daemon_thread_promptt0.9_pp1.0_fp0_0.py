import threading
# Test threading daemon as well.

from xonsh.tools import ON_WINDOWS
from xonsh.platform import HAS_PYGMENTS

from xonsh import __version__ as XONSH_VERSION
from xonsh.main import setup


class TestAMain:
    def test_default_args_with_site(self, xonsh_builtins, monkeypatch, tmpdir):
        args = ["xonsh", "-D", "-c", "exit"]
        old_xd = xonsh_builtins.__xonsh_data__
        monkeypatch.setattr(sys, "argv", args)
        xd = {}
        tools = {
            "evaler": {
                "env": {"XONSH_SHOW_TRACEBACK": "1", "XONSH_STORE_STDOUT": "1"},
                "ctx": {"XONSH_ENCODING": "utf-8", "XONSH_ENCODING_ERRORS": "surrogateescape"},
                "aliases": {},
                "update_env": False,
            },
            "shell":
