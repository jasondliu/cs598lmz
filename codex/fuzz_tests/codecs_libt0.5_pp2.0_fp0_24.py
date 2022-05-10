import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Handle timezone
import os
os.environ['TZ'] = 'UTC'

# This is needed to load models in the main program
from pkg_resources import resource_filename

# Import the main window object (mw) from aqt
from aqt import mw
# from aqt.utils import showInfo
# from aqt.qt import *

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

# We want to connect this function to the 'Tools' menu
action = QAction("Create copy of selected decks", mw)
mw.connect(action, SIGNAL("triggered()"), main)
mw.form.menuTools.addAction(action)

def main():
    mw.checkpoint("Create copy of selected decks")
    mw.progress.start()
    try:
        decks = mw.col.decks.all()
       
