import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

##
# @package utils
# @author Julien Bernard
# @author Alexandre Bonhomme
# @date 08 Juil. 2011
#
# This package contains everything useful to display windows and to
# manipulate PyGame objects (buttons, images, etc.).
#
# @package utils.button
# @author Julien Bernard
# @author Alexandre Bonhomme
# @date 08 Juil. 2011
#
# All buttons used in the game are manipulated thanks to the classes
# in this folder.
# 

##
# @file constants.py
# @author Julien Bernard
# @author Alexandre Bonhomme
# @date 08 Juil. 2011
#
# This file contains all constant used in the game.
#

## The sprite size in pixels.
SPRITE_SIZE_PX = 32

## The screen size in pixels.
SCREEN_SIZE_PX = WIDTH_SCREEN*SPRITE_SIZE_PX, HEIGHT_SCREEN*
