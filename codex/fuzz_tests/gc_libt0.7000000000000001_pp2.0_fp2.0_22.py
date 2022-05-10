import gc, weakref

class Test( object ):
    def __init__( self, name ):
        self.name = name

    def __del__( self ):
        print "----> remove %s" % self.name


def main():
    gc.set_debug( gc.DEBUG_LEAK )
    t1 = Test( "1" )
    t2 = Test( "2" )
    t3 = Test( "3" )
    t4 = Test( "4" )
    t5 = Test( "5" )
    t6 = Test( "6" )
    wr = weakref.ref( t6 )
    print wr()
    del t1
    del t2
    del t3
    del t4
    del t5
    del t6

    gc.collect()
    print wr()
    print gc.collect()

if __name__ == "__main__":
    main()
