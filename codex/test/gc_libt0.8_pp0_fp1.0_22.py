import gc, weakref

#-------------------------------------------------------------------------------
#  'TreeNode' class:
#-------------------------------------------------------------------------------

class TreeNode ( object ):
    """ Abstract base class for tree nodes in trees of Python objects.
    """

    #-- Public Methods ---------------------------------------------------------

    def __init__ ( self, children = None ):
        """ Initializes the object.
        """
        if children is not None:
            self.children = children
        else:
            self.children = []


    def add ( self, new_child ):
        """ Adds a child to the object's list of children.
        """
        self.children.append( new_child )


    def detailed_str ( self, prefix = '' ):
        """ Returns a detailed string representation of the object.
        """
        s = prefix + repr( self ) + '\n'
        for child in self.children:
            s += child.detailed_str( prefix + '  ' )

        return s


    def refresh ( self ):
        """ Refreshes the object.
        """
        pass


