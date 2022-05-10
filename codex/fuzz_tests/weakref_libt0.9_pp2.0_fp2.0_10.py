import weakref
import Gaffer
import GafferImage
import GafferScene
import GafferArnold
import GafferUI
import igor
import imath
__import__( "IECore" ).loadConfig( "GAFFER_STARTUP_PATHS", subdirectory = "GafferArnold" )
__import__( "IECore" ).loadConfig( "GAFFER_STARTUP_PATHS", subdirectory = "GafferImage" )
__import__( "IECore" ).loadConfig( "GAFFER_STARTUP_PATHS", subdirectory = "GafferUI" )
__import__( "IECore" ).loadConfig( "GAFFER_STARTUP_PATHS", subdirectory = "GafferScene" )
__import__( "IECore" ).loadConfig( "GAFFER_STARTUP_PATHS", subdirectory = "Gaffer" )

##########################################################################
# Metadata definition
##########################################################################

__nodeMenu__ = GafferUI.NodeMenu.defineSubMenu( "/Igor/Create Nodes/Arnold
