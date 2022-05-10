import types
types.MethodType(lambda self: None, None, None)

#  pylint: disable=unused-argument
def _mock_method(*args, **kwargs):
    """Mock method that does nothing."""
    pass

#  pylint: disable=unused-argument
def _mock_method_constant_return(*args, **kwargs):
    """Mock method that returns a constant value."""
    return True

#  pylint: disable=unused-argument
def _mock_method_constant_return_false(*args, **kwargs):
    """Mock method that returns a constant value."""
    return False

#  pylint: disable=unused-argument
def _mock_method_constant_return_none(*args, **kwargs):
    """Mock method that returns a constant value."""
    return None

#  pylint: disable=unused-argument
