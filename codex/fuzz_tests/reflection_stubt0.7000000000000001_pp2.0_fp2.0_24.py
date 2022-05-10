fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# TypeError: 'generator' object is not callable

fn = lambda: None
fn.__code__ = "abc"
fn()

# TypeError: 'str' object is not callable

fn = lambda: None
fn.__code__ = -1
fn()

# TypeError: 'int' object is not callable

fn = lambda: None
fn.__code__ = fn
fn()

# RecursionError: maximum recursion depth exceeded while calling a Python object

fn = lambda: 0
fn.__code__ = ()
fn()

# TypeError: 'tuple' object is not callable

fn = lambda: 0
fn.__code__ = {}
fn()

# TypeError: 'dict' object is not callable

fn = lambda: 0
fn.__code__ = []
fn()

# TypeError: 'list' object is not callable

fn = lambda: 0
fn.__code__ = b"abc"
fn()

# TypeError: 'bytes' object is not callable

