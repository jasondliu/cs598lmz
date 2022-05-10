gi = (i for i in ())
# Test gi.gi_code which is the code object associated with the generator
# and gi.gi_frame which is the frame object associated with the generator
print(gi.gi_code, gi.gi_frame)

# Test gi.gi_running. If a generator is executing, this is set to 1, else it is 0.
def coroutine():
    print('starting...')
    x = yield
    print('received:', x)

c = coroutine()
print(c.gi_running)
next(c)
print(c.gi_running)
c.send(42)
# c.close()

# Test gi.send(value)
# The send() method resumes the generator and “sends” a value into the generator function.
# The value argument becomes the result of the current yield expression.
# The send() method returns the next value yielded by the generator, or raises StopIteration if the generator exits without yielding another value. When send() is called to start the generator, it must be called with None as the argument, because there is no yield expression that could receive the value.

# Test gi
