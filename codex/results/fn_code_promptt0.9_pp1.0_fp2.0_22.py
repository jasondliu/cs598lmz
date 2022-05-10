fn = lambda: None
# Test fn.__code__.co_filename
# fn.__code__.co_filename is empty if fn is builtin (ex fn=len)
print "fn is builtin: ", inspect.isbuiltin(fn)
if inspect.isbuiltin(fn):
    co_filename = ""
else:
    co_filename = fn.__code__.co_filename
print "fn.__code__.co_filename:", repr(co_filename)


def filestat(filename):
    if not os.path.isabs(filename):
        filename = os.path.abspath(filename)
    stat = os.stat(filename)
    return {'size': stat.st_size, 'mtime': stat.st_mtime}
print "filestat:", filestat("example_call_with_args.py")
print "filestat:", filestat("example_obj_attr.py")


# TODO: Validate that filename exists
# TODO: Then it would be possible to validate that filename
# of function is in the current working directory
# This would mean that we don
