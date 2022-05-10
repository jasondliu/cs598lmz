fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__.co_code

# Issue #25216
real_gen_obj = iter(())
real_gen_obj.__name__ = "real_gen_obj"
real_gen_obj.__qualname__ = "real_gen_obj"


def fake_print(*values, sep=' ', end='\n', file=None, flush=False):
    print(*values, sep=sep, end=end, file=file, flush=flush)
    if flush:
        file.flush()

# Issue #29524: ensure that creating a FrameSummary uses the provided
# linecache.getlines to load lines, even if another instance of
# FrameSummary is created in the process that uses the default
# linecache.getlines.
linecache.getlines = fake_print
fs = d.extract_stack()[-1]
id(fs.linecache.getlines) == id(linecache.getlines)
