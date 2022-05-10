fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# https://bugs.python.org/issue39558
def test_c_code_obj_to_py_code_obj_with_code_object_as_code_object():
    class C:
        def __init__(self):
            self.__code__ = fn.__code__

    c = C()

    with raises(Exception):
        c.__code__.co_filename

    with raises(Exception):
        c.__code__.co_argcount

    with raises(Exception):
        c.__code__.co_consts


def test_c_code_obj_to_py_code_obj_with_code_object_as_code_object_with_file_line_name():
    class C:
        def __init__(self):
            self.__code__ = fn.__code__

    c = C()
    c.__code__ = fn.__code__

    assert c.__code__.co_filename == "<string>"
    assert c.__code__.co_argcount == 0
    assert c
