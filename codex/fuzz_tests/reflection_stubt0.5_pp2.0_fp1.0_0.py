fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
"""
    )
    result = testdir.runpytest()
    result.stdout.fnmatch_lines(["*1 failed*"])


def test_compile_error_with_syntax_error(testdir):
    """#1414"""
    testdir.makepyfile(
        """
        import pytest
        def test_foo():
            pytest.compile_error("def f():\n return 1 + ")
    """
    )
    result = testdir.runpytest()
    result.stdout.fnmatch_lines(["*1 failed*"])


def test_compile_error_with_syntax_error_in_function(testdir):
    """#1414"""
    testdir.makepyfile(
        """
        import pytest
        def test_foo():
            pytest.compile_error("def f():\n return 1 + ", function="f")
    """
    )
    result = testdir.runpytest()
    result.stdout.fnmatch_lines(["
