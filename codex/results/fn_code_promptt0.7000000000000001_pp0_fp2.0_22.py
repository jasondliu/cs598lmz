fn = lambda: None
# Test fn.__code__
fn.__code__ == ()
fn.__code__ == None
fn.__code__ == False
fn.__code__ == True
fn.__code__ == 0
fn.__code__ == 1
fn.__code__ == 0.0
fn.__code__ == 1.0
fn.__code__ == ''
fn.__code__ == 'a'
fn.__code__ == b'a'
fn.__code__ == ()
fn.__code__ == []
fn.__code__ == {}
fn.__code__ == {0: 0}

# Test fn.__code__.co_name
fn.__code__.co_name == ()
fn.__code__.co_name == None
fn.__code__.co_name == False
fn.__code__.co_name == True
fn.__code__.co_name == 0
fn.__code__.co_name == 1
fn.__code__.co_name == 0.0
fn.__code__.co_name == 1.0
fn.__code__.co_
