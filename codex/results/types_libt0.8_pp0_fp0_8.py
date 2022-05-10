import types
types.SimpleNamespace()

# Test library imports
import pytest

# Test imports
from ....backend.mpl import load_figure, load_image
from ....extern.six import BytesIO


def test_load_image():
    """Test that load_image doesn't fail."""
    with pytest.warns(UserWarning, match='matplotlib'):
        image = load_image(BytesIO(), 'png')
    assert image.shape[2] == 3
    assert image.dtype == np.uint8


def test_load_image_file_like_object(tmpdir):
    """Test that load_image doesn't fail for a file like object."""
    imgpath = tmpdir.join("test.png").strpath
    with open(imgpath, 'w') as fp:
        fp.write("dummy content, just to create the file")
    # We should not raise an error in this case
    with pytest.warns(UserWarning, match='matplotlib'):
        image = load_image(fp, 'png')
    assert
