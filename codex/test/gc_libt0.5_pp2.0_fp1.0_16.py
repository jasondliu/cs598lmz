import gc, weakref

#---------------------------------------------------------------------------
#  Define a 'no value' constant:
#---------------------------------------------------------------------------

NoValue = object()

#---------------------------------------------------------------------------
#  Returns a string of the form 'ClassName(name=value, ...)':
#---------------------------------------------------------------------------

def class_name_of ( object ):
    """ Returns a string of the form 'ClassName(name=value, ...)'.
    """
    return object.__class__.__name__ + '(%s)' % str( object )

#---------------------------------------------------------------------------
#  Returns a string of the form 'ClassName(name=value, ...)':
#---------------------------------------------------------------------------

def class_of ( object ):
    """ Returns a string of the form 'ClassName'.
    """
    return object.__class__.__name__

#---------------------------------------------------------------------------
#  Returns a string of the form 'ClassName(name=value, ...)':
#---------------------------------------------------------------------------

def repr_type ( object ):
    """ Returns a string of the form 'ClassName(name=value, ...)'.
    """
