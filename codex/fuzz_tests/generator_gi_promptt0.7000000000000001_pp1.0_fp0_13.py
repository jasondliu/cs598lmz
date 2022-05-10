gi = (i for i in ())
# Test gi.gi_code.co_filename attribute

import types
import os

def test_filename():
    gi = (i for i in ())
    file = gi.gi_code.co_filename
    assert isinstance(file, str)
    assert file == os.path.abspath(__file__)

test_filename()
