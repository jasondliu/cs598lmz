import weakref

from WebKit.Page import Page
from WebUtils import HTMLEncoder
from MidKit.SubThread import threadSince, threadEndTime

import Sidekick
from Sidekick import SKObject
from Sidekick.Threading import DummyThread, CurrentThread

#----------------------------------------------------------------------------

_globals = globals()
currentThread = CurrentThread

#----------------------------------------------------------------------------

class SidekickError(Exception): pass

#----------------------------------------------------------------------------
class InvalidThread(SidekickError):
	message = "The thread object you specified is not valid."
	
#----------------------------------------------------------------------------
class ThreadNotFound(SidekickError):
	message = "The specified thread was not found."

#----------------------------------------------------------------------------
class ThreadAlreadyStarted(SidekickError):
	message = "The thread could not be started because it is already running."

#----------------------------------------------------------------------------
class ThreadAlreadyCreated(SidekickError):
	message = "A thread already exists with the same name."

#----------------------------------------------------------------------------
class ThreadIDAlreadyCreated(SidekickError):
	message = "A thread already exists with the same ID."

#----------------------------------------------------------------------------
