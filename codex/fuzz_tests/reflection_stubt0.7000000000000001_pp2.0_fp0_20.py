fn = lambda: None
gi = (i for i in ())
fn.__code__ = lambda: None
gi.__code__ = lambda: None
fn.__code__.co_code = lambda: None
gi.__code__.co_code = lambda: None
fn.__code__.co_code = b'\x01'
gi.__code__.co_code = b'\x01'
fn.__code__.co_code = b'\x01\x00'
gi.__code__.co_code = b'\x01\x00'
fn.__code__.co_code = b'\x01\x00\x00'
gi.__code__.co_code = b'\x01\x00\x00'
fn.__code__.co_code = b'\x01\x00\x00\x00'
gi.__code__.co_code = b'\x01\x00\x00\x00'
fn.__code__.co_code = b'\x01\x00\x00\x00\x00'
gi.__code__.co_code = b'
