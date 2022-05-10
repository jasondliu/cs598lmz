fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

fn.__code__ = gi.gi_code.co_code
fn()

fn.__code__ = gi.gi_code.co_consts
fn()

fn.__code__ = gi.gi_code.co_filename
fn()

fn.__code__ = gi.gi_code.co_firstlineno
fn()

fn.__code__ = gi.gi_code.co_flags
fn()

fn.__code__ = gi.gi_code.co_freevars
fn()

fn.__code__ = gi.gi_code.co_name
fn()

fn.__code__ = gi.gi_code.co_names
fn()

fn.__code__ = gi.gi_code.co_nlocals
fn()

fn.__code__ = gi.gi_code.co_stacksize
fn()

fn.__code__ = gi.gi_code.co_varnames
fn()

fn.
