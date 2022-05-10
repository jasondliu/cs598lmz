fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# In[ ]:

# -----------------------------------------------------------------------------
#
#                            Unittests
#
# -----------------------------------------------------------------------------

def test_unaryop_is_not_null():
    """
    Test the output of the unary operator is_not_null.
    """
    lhs = np.array([False, False, True, True])
    rhs = np.array([False, False, False, True])
    got = lhs != rhs
    expect = np.array([False, False, True, False])
    np.testing.assert_equal(got, expect)
    return

def test_unaryop_is_not_null_scalar():
    """
    Test the output of the unary operator is_not_null.
    """
    lhs = np.array([False, False, True, True])
    rhs = False
    got = lhs != rhs
    expect = np.array([True, True, True, True])
    np.testing.assert_equal(got, expect)
    return

def test
