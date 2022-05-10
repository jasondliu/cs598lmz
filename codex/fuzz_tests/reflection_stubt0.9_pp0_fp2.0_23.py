fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


def test_try_finally():
    # Make sure execution leaves both blocks, not just one or the
    # other.

    # The reason this is important is obscure.  Consider this
    # code, similar to that found in the marshal module:

    #     while 1:
    #         op = read_byte()
    #         if op == STOP: return
    #         dispatch[op]()

    # If the dispatch is a dict lookup, it's possible that the opcode
    # is invalid, leading to an exception.  However, there's a subtle
    # problem with this code as written.  After an exception is
    # raised, the fina
