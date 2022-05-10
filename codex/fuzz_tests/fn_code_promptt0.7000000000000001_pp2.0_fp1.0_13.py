fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = 42
# AttributeError: readonly attribute

fn = lambda: None
# Test fn.__code__.co_freevars
fn.__code__.co_freevars = 42
# AttributeError: readonly attribute

fn = lambda: None
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = 42
# AttributeError: readonly attribute

fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = 42
# AttributeError: readonly attribute

fn = lambda: None
# Test fn.__code__.co_name
fn.__code__.co_name = 42
# AttributeError: readonly attribute

fn = lambda: None
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 42
# AttributeError: readonly attribute

fn = lambda: None
# Test fn.__code
