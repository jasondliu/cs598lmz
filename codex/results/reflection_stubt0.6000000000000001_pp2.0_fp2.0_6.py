fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# function object with strange __code__ object
def strange_fn():
    pass
strange_fn.__code__ = 42

# function object with strange __code__ object
def strange_fn2():
    pass
strange_fn2.__code__ = {}


# class object with strange __dict__
class strange_class(object):
    pass
strange_class.__dict__ = 42

# class object with strange __dict__
class strange_class2(object):
    pass
strange_class2.__dict__ = {}

# class object with strange __bases__
class strange_class3(object):
    pass
strange_class3.__bases__ = 42

# class object with strange __bases__
class strange_class4(object):
    pass
strange_class4.__bases__ = ()

# class object with strange __name__
class strange_class5(object):
    pass
strange_class5.__name__ = 42

# class object with strange __name__
class strange
