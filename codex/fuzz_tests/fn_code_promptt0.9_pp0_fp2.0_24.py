fn = lambda: None
# Test fn.__code__.__class__.co_filename == "<stdin>"
# See https://bugs.python.org/issue34523.
fn.__code__.__class__.co_filename = "<stdin>"
assert fn() is None


class G:
    pass


def f():
    """Test ast recognition of global statements."""

    global G
    G = 10


def g():
    """Test ast recognition of nonlocal statements."""

    G.y = 10


# Test that ast accepts a lambda expression as the body of a class def
ast.parse("""class C: __slots__ = lambda self: ()""")

# Test that ast accepts coercing to (Class)Def()
ast.parse(ast.Expression(ast.Lambda())).body.args.args[0]

# Test that ast accepts coercing to Module()
ast.parse(ast.Expression(ast.Lambda())).body.body

# Test that ast.PyCF_ONLY_AST returns an AST
assert isinstance(compile('pass', '', 'exec', ast.PyCF
