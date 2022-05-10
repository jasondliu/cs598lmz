fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# This is a bit of a hack, but it lets us get the line number easily
def lineno(item):
    try:
        return item.gi_frame.f_lineno
    except AttributeError:
        return item.__traceback__.tb_lineno

def check_line_numbers(f, start, count):
    for i, item in enumerate(f, start):
        if lineno(item) != i:
            print('%s is on line %d, should be %d' % (item, lineno(item), i))

# f_back points to previous frame object (towards the caller)
def descend_frames(f):
    while f:
        print(f)
        f = f.f_back
    print(f)

def show_stack(f, context=1):
    for i in range(context):
        f = f.f_back
    descend_frames(f)

def show_stack_context(f, context=1):
    descend_frames(f.
