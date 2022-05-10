fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.undefined = gi.__code__ = gi.gi_frame = 0

# this function is used to transform a function into a coroutine.
# it returns a coroutine object, which can be used to proceed to the
# next breakpoint.

def insert_yield(fn):

    # the first time insert_yield is used for a function, we record a
    # few pieces of information about it, which we later need for
    # analysis and rewriting.

    if not hasattr(fn, 'undefined'):

        # note that the function's closure contains the loop variable
        # of the enclosing for-loop, so we have to walk the entire
        # stack.

        try:
            f_back = fn.__code__.co_freevars.index("f_back")
        except ValueError:
            f_back = -1

        # to create a coroutine, we need to rewrite the function's
        # bytecode, as well as create a new code object.

        code = Code(
            fn.__code__.co_argcount,
            fn
