fn = lambda: None
# Test fn.__code__
fn.__code__
# Test fn.__code__.co_code
fn.__code__.co_code
# Test fn.__code__.co_code.decode
fn.__code__.co_code.decode('utf-8')
# Test fn.__code__.co_code.decode with invalid argument
fn.__code__.co_code.decode('xxx')
# Test fn.__code__.co_code.decode with invalid argument
fn.__code__.co_code.decode('utf-8', 'strict')
# Test fn.__code__.co_code.encode
fn.__code__.co_code.encode('utf-8')
# Test fn.__code__.co_code.encode with invalid argument
fn.__code__.co_code.encode('xxx')
# Test fn.__code__.co_code.encode with invalid argument
fn.__code__.co_code.encode('utf-8', 'strict')
# Test fn.__code__.co_code.
