fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Exercise: assign to a lambda
(lambda: None).__code__ = (i for i in ())

# Exercise: assign to a lambda, then call it
(lambda: None).__code__ = (i for i in ())
(lambda: None)()

# Exercise: assign to a lambda, then call it, then call it again
(lambda: None).__code__ = (i for i in ())
(lambda: None)()
(lambda: None)()

# Exercise: assign to a lambda, then call it, then call it again, then call it a third time
(lambda: None).__code__ = (i for i in ())
(lambda: None)()
(lambda: None)()
(lambda: None)()

# Exercise: assign to a lambda, then call it, then call it again, then call it a third time, then call it a fourth time
(lambda: None).__code__ = (i for i in ())
(lambda: None)()
(lambda: None)()
(lambda: None)()
(lambda: None)()

#
