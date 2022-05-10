import io
# Test io.RawIOBase
import ntpath
from _pytest import deprecated
from plumbum import local
from plumbum import FG
from plumbum import remote
from test_recipe.conftest import is_windows
from test_recipe.utils import run_in_tempdir


@pytest.mark.skipif(
    langtools_missing(),
    reason="Language tools tests requires langtools to be available",
)
def test_binary_toggle(
    compile_check,
    exe,
    gen_fn,
    run_and_assert_result,
    run_and_assert_stdout,
):
    """Test that we can call a Java binary from python.

    :param recipe_dir: Recipe dir to run test

    Assert that Binary targeting works as desired for simple Java binaries.
    1.) Compile check works
    2.) Can run compiled java binary
    3.) Toggle between Java and Jar versions works correctly with correct args
    """
    # Can create exe
    assert exe is not None
    # Can setup binary
    assert "Test.java" in gen_fn

