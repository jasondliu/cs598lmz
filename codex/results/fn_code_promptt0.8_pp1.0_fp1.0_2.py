fn = lambda: None
# Test fn.__code__
fn.__code__ = None

# pylint: disable=no-member
class TestCode:
    """Test code object."""

    def test_no_code(self):
        """Test no code object"""
        def test():
            """Test function"""
            pass
        test.__code__ = None
        try:
            assert_code_equal(False, test.__code__, test)
            assert_code_equal(False, test.__code__, test, ignore_source=True)
        except AssertionError as exception:
            assert 'py_code' in str(exception)
        else:
            raise AssertionError

    def test_no_ob_code(self):
        """Test no ob_code"""
        def test():
            """Test function"""
            pass
        test.__code__.co_code = None
        try:
            assert_code_equal(False, test.__code__, test)
            assert_code_equal(False, test.__code__, test, ignore_source=True)
        except Ass
