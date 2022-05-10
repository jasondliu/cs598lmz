from types import FunctionType
list(FunctionType(lambda:"f",{},"",()).__closure__)

""" closure is an attribute which gives details about closure.
    It is a tuple of cell objects and stores references if any.
    A cell object is used to store a reference to an object which is then used in a closure"""

"""lambda:"f",{},"",()
    [<cell at 0x0365C798: str object at 0x03641820>]""",

"""
    FunctionType is an inbuilt datatype.

    f<x> = lambda x:x+x

        f<x>.__closure__
        (<cell at 0x033A4998: int object at 0x02F7EBB0>,)
    """
# Variable-length Argument
"""   nums = (1,2,3,4,5)

    sqr = lambda *args: [x**2 for x in args]

    print(sqr(*nums))
    
    
        sqr = lambda x,y,z,*args: [arg**2 for arg in args]
        
        print(sqr[1,2
