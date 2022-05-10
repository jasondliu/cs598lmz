fn = lambda: None
# Test fn.__code__ capability
fn.__code__ = foo
# Test fn.co_code capability
fn.co_code = b"foo"
# Test dis.code_info() capability
fn.co_code = dis.code_info(
