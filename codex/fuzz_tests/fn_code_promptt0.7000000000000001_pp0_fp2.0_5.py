fn = lambda: None
# Test fn.__code__ exists, so we don't get a crash.
fn.__code__

# Test that we can get a code object from a function.
co = fn.__code__

# Test that we can get the source of the code object.
print(inspect.getsource(co))

# Test that the source is valid Python.
ast.parse(inspect.getsource(co))

# Test that we can get the source of a module.
import inspect_test
print(inspect.getsource(inspect_test))

# Test that the source is valid Python.
ast.parse(inspect.getsource(inspect_test))

# Test that we can get the source of a traceback frame.
try:
    raise Exception()
except Exception:
    f = sys.exc_info()[2].tb_frame
print(inspect.getsource(f))

# Test that the source is valid Python.
ast.parse(inspect.getsource(f))

# Test that we can get the source of a class.
lo = locals()
exec("""
class C
