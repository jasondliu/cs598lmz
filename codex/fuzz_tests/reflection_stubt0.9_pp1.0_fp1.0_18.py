fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
serialise(fn)

fn = lambda: None
gi = (i for i in ())
gi.gi_frame = None
fn.__code__ = gi
serialise(fn)

fn = lambda: None
gi = (i for i in ())
f = lambda: None
gi.gi_frame = f
fn.__code__ = gi
serialise(fn)

fn = lambda: None
gi = (i for i in ())
f = lambda: None
f.f_code = None
gi.gi_frame = f
fn.__code__ = gi
serialise(fn)

fn = lambda: None
gi = (i for i in ())
f = lambda: None
c = lambda: None
f.f_code = c
gi.gi_frame = f
fn.__code__ = gi
serialise(fn)

fn = lambda: None
gi = (i for i in ())
gi.gi_running = True
f = lambda: None
c = lambda: None
f.f_code = c
gi.gi_frame =
