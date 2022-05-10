fn = lambda: None
# Test fn.__code__.co_filename on Python 2.
    try:
        co_filename = fn.__code__.co_filename
    except AttributeError:
        pass
    else:
# Warn about importing from the stdlib.
        filename = getattr(fn, '__cached__', None) or co_filename
        if not filename:
            return
        if filename[:1] + filename[-1:] == '<>':
            filename = os.path.splitext(co_filename)[0] + filename[1:-1]
        if _co_filename_fn(filename):
            return
        if filename.startswith('<frozen '):
            return
        if filename.startswith(prefix):
            return
        if 'site-packages' in filename:
            return
        if 'dist-packages' in filename:
            return
        if 'python%d.%d' % sys.version_info[:2] in filename:
            return
        if 'lib/python' in filename:
            return
        if hasattr(sys, 'real_prefix'):

