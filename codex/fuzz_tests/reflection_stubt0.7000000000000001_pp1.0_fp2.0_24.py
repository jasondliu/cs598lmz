fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

try:
    fn()
except TypeError as e:
    print(e)

try:
    fn.__code__ = gi
except TypeError as e:
    print(e)

try:
    fn()
except TypeError as e:
    print(e)
"""
    assert exc.exception.args[0] == (
        "can't set attributes of built-in/extension type 'function'"), exc.exception.args[0]


def test_set_code_co_filename(space):
    w_res = space.execute("""if (typeof __filename !== 'undefined') {
                                 var fn = function() {};
                                 fn.__code__.co_filename = fn;
                                 return fn.__code__.co_filename;
                             }""")
    assert space.str_w(w_res) == "fn", space.str_w(w_res)


def test_new_code(space):
    w_res = space.execute("""if (type
