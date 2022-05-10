import mmap
import os
import shutil
import warnings

import pytest

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFile


# Test helpers.

def _assert_warning():
    from PIL import ImageFile

    with pytest.warns(UserWarning):
        ImageFile.LOAD_TRUNCATED_IMAGES = False
        im = Image.open(
            "Tests/images/iss634.png"
        )  # Missing IDAT chunk, should be truncated.
        im.load()
        assert im.mode == "RGB"


def _assert_no_warning():
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    im = Image.open(
        "Tests/images/iss634.png"
    )  # Missing IDAT chunk, should be truncated.
    with pytest.warns(None) as record:
        im.load()
    assert len(record) == 0

