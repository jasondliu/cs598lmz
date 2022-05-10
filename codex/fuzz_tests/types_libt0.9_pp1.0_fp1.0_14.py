import types
types.SimpleNamespace(**vars(nn.functional))

import pytest

from collections.abc import Iterable

from lucid.misc.io import *
from lucid.misc.io.reading import dummy_path
from lucid.misc.io.reading import load
from lucid.misc.io.serialize import load_serialized
from lucid.misc.io.serialize import save_serialized
from lucid.misc.io.serialize import save_serialized_record
from lucid.misc.io.serialize import save_serialized_record_string
import lucid.misc.io.showing as showing

from mock import patch
from tempfile import NamedTemporaryFile
import contextlib


def test_load():
  with open("test", "w") as fh:
    fh.write("python")
  assert load("test") == "python"


def test_dummy_path():
  with pytest.raises(OSError):
    dummy_path("flabergast")

  with pytest.raises(OSError):
    dummy_path("flabergast", create
