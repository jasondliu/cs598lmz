fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()"""


def test_code_object_attribute_error():
    """Code objects should raise AttributeError when an unknown attribute is requested"""

    pytest.raises(AttributeError, lambda: code_object.__unknown_attribute__)


def test_code_object_repr():
    """Code objects should have a __repr__ method"""

    assert repr(code_object) == "<code object test_code_object_repr at 0x{0:x}, file '{1}', line 1>".format(
        id(code_object) & 0xFFFFFFFF, __file__
    )


def test_code_object_is_code():
    """Code objects should have an is_code attribute"""

    assert code_object.is_code is True


def test_code_object_is_code_object():
    """Code objects should have an is_code_object attribute"""

    assert code_object.is_code_object is True


def test_code_object_is_frame():
    """Code objects should have an is_frame attribute"""


