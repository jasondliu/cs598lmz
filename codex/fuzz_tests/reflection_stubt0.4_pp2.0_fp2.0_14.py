fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# crash
def fn():
    try:
        yield
    finally:
        pass
fn()

# crash
def fn():
    try:
        yield
    except:
        pass
fn()

# crash
def fn():
    try:
        yield
    except:
        pass
    finally:
        pass
fn()

# crash
def fn():
    try:
        yield
    except:
        pass
    else:
        pass
fn()

# crash
def fn():
    try:
        yield
    except:
        pass
    else:
        pass
    finally:
        pass
fn()

# crash
def fn():
    try:
        yield
    finally:
        pass
    else:
        pass
fn()

# crash
def fn():
    try:
        yield
    except:
        pass
    finally:
        pass
    else:
        pass
fn()

# crash
def fn():
    try:
        yield
    finally:
        pass
    except:
