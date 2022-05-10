import threading
threading.Thread(target=lambda: None).start()

# Import the main window object (mw) from ankiqt
from aqt import mw
# Import the "show info" tool from utils.py
from aqt.utils import showInfo
# Import all of the Qt GUI library
from aqt.qt import *

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def testFunction():
    # Get the number of cards in the current collection, which is stored in
    # the main window
    cardCount = mw.col.cardCount()
    # Show a message box
    showInfo("Card count: %d" % cardCount)

# Create a new menu item, "test"
action = QAction("test", mw)
# Set it to call testFunction when it's clicked
mw.connect(action, SIGNAL("triggered()"), testFunction)
# Add it to the tools menu
mw.form.menuTools.addAction(action)
