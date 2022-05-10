fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

fn = lambda: None
gi = (i for i in ())
gi.gi_code = gi
fn()

fn = lambda: None
gi = (i for i in ())
gi.gi_frame = gi
fn()

fn = lambda: None
gi = (i for i in ())
gi.gi_yieldfrom = gi
fn()

fn = lambda: None
gi = (i for i in ())
gi.gi_running = gi
fn()

fn = lambda: None
gi = (i for i in ())
gi.gi_frame.f_code = gi
fn()

fn = lambda: None
gi = (i for i in ())
gi.gi_frame.f_back = gi
fn()

fn = lambda: None
gi = (i for i in ())
gi.gi_frame.f_builtins = gi
fn()

fn = lambda: None
gi = (i for i in ())
gi.gi_frame.f_globals = gi
fn()

fn = lambda
