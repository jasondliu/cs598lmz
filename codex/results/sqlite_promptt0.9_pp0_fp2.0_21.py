import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections
############################################
# GLOBAL VARIABLES
############################################

# Colors
BLACK     = (0  ,0  ,0  )
WHITE     = (255,255,255)

BLUE      = (0  ,0  ,255)
GREEN     = (0  ,255,0  )
RED       = (255,0  ,0  )
CYAN      = (0  ,255,255)
PURPLE    = (255,0  ,255)
YELLOW    = (255,255,0  )

#Screen dimensions
SCREEN_WIDTH    = 800
SCREEN_HEIGHT   = 600
BGCOLOR          = BLACK

velocity = 1

p1score = 0
p2score = 0


batwidth       = 10
batlength      = 75
batminlength   = 50
batmaxlength   = 150
batmargin      = 30
batheight      = 10
batout         = True

p1_bat         = pygame.Rect(batmargin,0,batlength,batheight)
