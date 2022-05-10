fn = lambda: None
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno
def fn(): None
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno
"""
        self.assertNoErrors(output)


@skipUnless(BO_MAJOR)
class TestKnownBrokenPyPy(BaseTest):
    """Failures expected when executing against PyPy."""

    def test_dir_unicode(self):
        output = self.run_flake8(u('dir(u("a"))'))
        self.assertNoErrors(output)

    def test_except_missing_as(self):
        # We can only detect this error if you are running against PyPy
        output = self.run_flake8(
            textwrap.dedent("""
                            try:
                                1
                            except Exception:
                                pass
            """))
        self.assertError(output, E722)

    def test_except_with_multiple_arguments(self):
        output = self.run_flake8(
