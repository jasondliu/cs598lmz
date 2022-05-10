import codecs
codecs.register_error("strict", codecs.ignore_errors)

#
#   Globals
#

thisDir = os.path.dirname(__file__)
thisDir = os.path.abspath(thisDir)

mibBuilder = builder.MibBuilder()

testMibs = []

#
#   Support for loading MIBs
#

def loadMibs( *names ):
    global testMibs
    for name in names:
        if name not in testMibs:
            mibBuilder.loadModules( name )
            testMibs.append( name )

def loadMibsNoProxy( *names ):
    global testMibs
    for name in names:
        if name not in testMibs:
            mibBuilder.loadModules( name,
                proxyLoader=loader.NoProxyLoader() )
            testMibs.append( name )

def getMibPath( *names ):
    return os.pathsep.join( map( lambda x: os.path.join( thisDir, 'MI
