import gc, weakref

#-------------------------------------------------------------------------------
#  'DragAndDrop' class:
#-------------------------------------------------------------------------------

class DragAndDrop ( HasPrivateFacets ):
    """ Supports drag-and-drop operations for the Traits UI.
    """

    #-- Facet Definitions ------------------------------------------------------

    # The type of object to drag:
    drag_type = Trait( Instance( object ) )

    # The data to drag:
    data = Trait( None, None, Instance( HasFacets ) )

    # The viewer being dragged from (if any):
    source = Any

    # The viewer being dropped on (if any):
    target = Any

    # The name of the method called on the target to do the drop:
    set = Str

    # The name of the method called on the target to clear out any existing
    # data before a drop occurs:
    clear = Str

    # The name of the method called to determine if a drop is valid:
    is_valid = Str

    # Should a 'copy' operation be used instead of a 'move' operation?
    copy = Bool( False )

    # Comp
