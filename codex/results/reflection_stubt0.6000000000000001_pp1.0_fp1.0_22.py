fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# issue #3 - infinite loop in _getattrs
def func(): pass
func.__code__ = object()
func()

# issue #4 - infinite loop in _getattrs
def func(): pass
func.__code__ = 42
func()

# issue #5 - infinite loop in _getattrs
def func(): pass
func.__code__ = -42
func()

# issue #6 - infinite loop in _getattrs
def func(): pass
func.__code__ = 0
func()

# issue #7 - infinite loop in _getattrs
def func(): pass
func.__code__ = 1
func()

# issue #8 - infinite loop in _getattrs
def func(): pass
func.__code__ = 'a'
func()

# issue #9 - infinite loop in _getattrs
def func(): pass
func.__code__ = 'abc'
func()

# issue #10 - infinite loop in _getattrs
def func(): pass
func.__code__ = 'a' * 123
func()
