import weakref
import datetime

# Scripted object creation
import bge.logic
import mathutils

import GameLogic

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#
# Class definition
#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class Player:

	#
	# Constants
	#
	# all from Player.h

	NO_ACTION			= 0
	ACTION_SUBMIT		= 1
	ACTION_DEATH		=
