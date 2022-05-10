fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
gi.gi_frame = {}
gi.gi_code = {}
gi.gi_frame.f_globals = {'__builtins__': builtins}
gi.gi_code.co_flags = set()
gi.gi_code.co_varnames = set()
fn.__code__.co_flags = set()
fn.__code__.co_varnames = set()
fn.__code__.co_flags.update({'co_for_iter'})
fn.__code__.co_varnames.update({'i'})
fn()
"""
    )

    # Make sure we don't crash on this code. See Issue #12.
    # This used to crash because i is not a local variable, it is an
    # implicit parameter.
    tree, errors = _parse_to_ast(
        code=dedent(
            """\
            def fn():
                for i in range(3):
                    i
            """
        )
    )
    assert errors == []
