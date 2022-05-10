import types
types.MethodType(lambda self: self.x, None, A)

# TODO:
#   - test that the same method can be bound to two different instances
#   - test that a bound method can be rebound to a different instance
#   - test that the same method can be bound to two different classes
#   - test that a bound method can be rebound to a different class
#   - test that a bound method can be rebound to an instance of a subclass
#   - test that a bound method can be rebound to a subclass
#   - test that a bound method can be rebound to a superclass
#   - test that a bound method can be rebound to an instance of a superclass
#   - test that a bound method can be rebound to a different method
#   - test that a bound method can be rebound to a different function
#   - test that a bound method can be rebound to a different classmethod
#   - test that a bound method can be rebound to a different staticmethod
#   - test that a bound method can be rebound to a different property
#   - test that a bound method can be rebound to a different classmethod
#   -
