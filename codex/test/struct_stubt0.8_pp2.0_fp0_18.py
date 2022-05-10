from _struct import Struct
s = Struct.__new__(Struct)
s.size = Struct.size
s.format = Struct.format
s.pack = Struct.pack


def toutf8( s ):
    if isinstance( s, unicode ):
        return s.encode( 'utf-8' )
    return s

def toStr( s ):
    if not isinstance( s, basestring ):
        return str( s )
    return s

def flush_file( f ):
    # flush is not available on some non-buffered file-like objects
    try:
        f.flush()
    except:
        pass

def mkdir( dir ):
    if not os.path.isdir( dir ):
        os.makedirs( dir )

def mkdir_p( dir ):
    return mkdir( dir )

def realpath( path ):
    return os.path.abspath( os.path.expanduser( path ) )
