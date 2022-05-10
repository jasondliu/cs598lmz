import signal
# Test signal.setitimer()
import select
# Test select.select()
import tempfile

# Very basic test.  Make sure we can import the module, and make sure
# the kind() function selects the right kind for various inputs.


def test_import_module():
    """Import the Cython modules"""
    import glue.cythonutils
    import glue.cythonutils.cy_callback
    import glue.cythonutils.cy_window_timer


def test_get_kind():

    from glue.cythonutils import kind

    assert kind(False) == 'bool'
    assert kind(True) == 'bool'
    assert kind(1) == 'int'
    assert kind(2**64) == 'int'
    assert kind(np.array([])) == 'array'
    assert kind(np.array([2])) == 'array'
    assert kind(np.array([1, 2])) == 'array'
    assert kind(np.array([1, 2, 3])) == 'array'
    assert kind(np.array(['a', 'b', 'c']
