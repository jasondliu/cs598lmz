import weakref

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *

from Orca.vars import S
from Orca.utils import QT4_WaitCursorManager, getUserName, GetApplicationState
from Orca.utils import isScriptModified, notifyScriptModifiedState



# [[[TODO: WDW - this is a hack of the old pickling stuff.  This
# seems like a better approach, but I'm not sure it's better.
#
# We need to figure out a way to get rid of the audio.EventManager,
# and to have scripts be able to generate their own events.  But
# it seems like a script will need to have a reference to the
# event manager in order to create events.  And we need events to
# create scripts.  Hmmm.  Maybe the scripts need to be their own
# event manager.  Then the Orca event manager could take on the
# events that are specific to Orca.
#
# But the key is to get rid of
