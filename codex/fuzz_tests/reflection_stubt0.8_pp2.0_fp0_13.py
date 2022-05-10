fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = types.CodeType(0, 0, 0, 0, b'', b'', 0, b'', (), (), (), '', '', 0, b'')
cdc = gi.gi_code  # This takes a reference
gi.gi_frame = Frame(fn)
f = gi.gi_frame.f_back
gi.gi_frame.f_back = None
gi.gi_next = None
gi.gi_running = False
gi.gi_frame.f_lasti = -1
gi.gi_yieldfrom = None

b' '.join((
    # fn.func_name,
    ''.join(traceback.format_list([(cdc.co_filename, cdc.co_firstlineno, '', '')])).split('\n')[-2].lstrip(),
    ''.join([
        linecache.getline(cdc.co_filename, i).rstrip()+'\n'
        for i in range(1, cdc.co_firstlineno+1)
    ]),

