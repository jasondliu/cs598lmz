from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = _decompress

@pytest.fixture
def tempdircwd(tmpdir_factory):
    """Get a py.path.local to a temporary directory.
    The path is yielded, and the directory is removed on completion.

    The directory is also made the current working directory.
    Upon completion, the original current working directory is restored.
    This can work on Windows as well (py.test fixture magic).

    For more details, see http://pytest.org/latest/tmpdir.html

    Args:
        tmpdir_factory: pytest fixture to create a temporary directory
    """
    cwd = os.getcwd()
    tmpdir = py.path.local(str(tmpdir_factory.mktemp('data')))
    os.chdir(str(tmpdir))
    yield tmpdir
    os.chdir(cwd)
    tmpdir.remove(rec=1)


def test_temp_dir(tempdircwd):
    """Test that the temporary directory exists.
    """
    assert tempdircwd.check()
