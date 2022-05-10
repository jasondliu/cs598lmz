fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__.co_argcount

fn.__code__.co_argcount = 10
fn.__code__.co_argcount

fn.__code__.co_argcount = -1
fn.__code__.co_argcount

# Test fn.__code__.co_nlocals
fn.__code__.co_nlocals

fn.__code__.co_nlocals = 10
fn.__code__.co_nlocals

fn.__code__.co_nlocals = -1
fn.__code__.co_nlocals

# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize

fn.__code__.co_stacksize = 10
fn.__code__.co_stacksize

fn.__code__.co_stacksize = -1
fn.__code__.co_stacksize

# Test fn.__code__.co_flags
fn.__code__.co_flags

