import weakref
# Test weakref.ref(a) doesn't keep a alive
#
# The 'a' variable is created in a function, and should
# be cleared when the function exits.
#
# If the weak reference keeps 'a' alive, we'll see the
# "exit" message when the function returns, which it
# shouldn't.
#
# If 'a' is collected, we won't see the "exit" message,
# which we should.

# This test is intended to be run with the -A option,
# which enables reference counting.

def g():

    class A:

        def __del__(self):
            print('exit')
    a = A()
    weakref.ref(a)
    return


g()
print('ok')
