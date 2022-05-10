import weakref


#-------------------------------------------------------------------------------
#  'ToolbarEditor' class:
#-------------------------------------------------------------------------------

class ToolbarEditor ( BasicEditorFactory ):
    List      = Any
    auto_set  = Bool( True )
    update    = ATheme( '@std:tb_refresh' )
    click     = ATheme( '@std:tb_refresh' )
    _toolbar  = Instance( ToolBar, () )

    #---------------------------------------------------------------------------
    #  Trait definitions:
    #---------------------------------------------------------------------------

    klass = Instance( 'enthought.traits.ui.toolkit.ToolkitEditorFactory' )

    #---------------------------------------------------------------------------
    #  Transient 'add' event:
    #---------------------------------------------------------------------------

    add = Event

    #---------------------------------------------------------------------------
    #  Initializes the object:
    #---------------------------------------------------------------------------

    def __init__ ( self, *args, **traits ):
        self._text = {}
        self._ttip = {}
        self._image = {}
        self._method = {}
        self._name = {}
        self._content = {}
        super( Toolbar
