fn = lambda: None
# Test fn.__code__
fn.__code__
# Test fn.__code__.__globals__
fn.__code__.__globals__
# Test fn.__code__.__globals__.items()
globals_dict = fn.__code__.__globals__
globals_dict.keys()
# Test fn.__code__.__globals__['None']
fn.__code__.__globals__['None']
# Test fn.__code__.__globals__['None'].__class__
fn.__code__.__globals__['None'].__class__
# Test fn.__code__.__globals__['None'].__class__.__bases__
fn.__code__.__globals__['None'].__class__.__bases__
# Test fn.__code__.__globals__['None'].__class__.__bases__[0]
fn.__code__.__globals__['None'].__class__.__bases__[0]

