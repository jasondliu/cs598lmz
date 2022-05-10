import types
types.new_class( 'MyClass'
               , (object,) 
               , dict( class_method = classmethod( lambda *args: "class method" )
                     , instance_method = lambda *args: "instance method"
                     , class_attribute = "value"
                     , instance_attribute = property( lambda self: "instance attribute" )
                     )
               )
class AnotherClass( object ):

    @classmethod
    def class_method( cls, *args ):
        return "class method"
    
    def instance_method( self, *args ):
        return "instance method"
    
    def get_instance_attribute( self ):
        return "instance attribute"
    
    instance_attribute = property( fget = get_instance_attribute )
    
    class_attribute = "value"

import time

class Test( object ):

    def __call__( self, method ):
        
        def run_test():
            start = time.time()
            method()
            return time.time() - start
        
        return run_test

test = Test()


