import weakref
# Test weakref.ref_create and weakref.ref_create_keyed

# The tests we use here mostly check the _weakref module internals,
# as well as the C API.  But they do also check that the Python
# interface defined by weakref.py itself is correct.


def has_key(d, key):
    try:
        d[key]
        return True
    except KeyError:
        return False

def make_test():
    """Return an object with a finalizer that sets attribute attrname to 1."""
    ref_list = []
    last_id = 0
    class Test:
        def __del__(self):
            nonlocal last_id, ref_list
            my_id = id(self)
            last_id = my_id
            ref_list.append(my_id)
    return Test(), ref_list, last_id

def test_callback_invalid_args():
    # Check that invalid callback arguments raise TypeError
    ob, ref_list, last_id = make_test()
    # Invalid callback
    try:
       
