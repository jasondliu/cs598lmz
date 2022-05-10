import select
import socket
import sys
import threading
import time

import pytest

from pyngrok import ngrok


def test_ngrok_version():
    """Test that the ngrok version is correctly parsed."""
    version = ngrok.get_ngrok_version()
    assert isinstance(version, tuple)
    assert len(version) == 3


def test_ngrok_version_error():
    """Test that an error is raised when the ngrok version cannot be parsed."""
    with patch("pyngrok.ngrok.check_output", return_value="not a version"):
        with pytest.raises(ValueError):
            ngrok.get_ngrok_version()


def test_ngrok_version_check():
    """Test that the ngrok version is checked."""
    with patch("pyngrok.ngrok.get_ngrok_version", return_value=(1, 0, 0)):
        with pytest.raises(RuntimeError):
            ngrok.check
