import types
types.BottomType = types.ModuleType( "bottom" )

class Bottom( object ):
    def __init__( self ):
        setattr( types.BottomType, ("x" + str( random.randint( 1, (1 << 30) ) )),
                 types.BottomType )
    def __repr__( self ):
        return "_|_"
bottom = Bottom()

def to_bdd( f ):
    global bdd_to_func
    if f in bdd_to_func:
        return bdd_to_func[f]
    if f is True:
        return bdd.TRUE
    if f is False:
        return bdd.FALSE
