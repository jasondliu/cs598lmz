import types
types.MethodType(callback, window)    # Attach as a method
window.callback()                     # Run the callback

# Now it's a bound method and the callback has access to the window instance
# As it's argument.
window.__dict__

# Assign the same bound method to the child
window.child.method = window.method
window.child.method() # This runs callback too!

# The Python language supports a form of multiple inheritance as well.
# A class definition with multiple base classes looks like this:
#
# class DerivedClassName(Base1, Base2, Base3):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>
#
# For example, the following code will define a new class,
# which is the derived class of three other classes:
#
# class Base1:
#     pass
#
# class Base2:
#     pass
#
# class Base3:
#     pass
#
# class DerivedClassName (Base1, Base2, Base3):
#     pass
#

