import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import gobject
gobject.threads_init()

import dbus
import dbus.service
import dbus.mainloop.glib
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

from debug import log
from config import config

from dbus_session import DBusSession

def main(argv):
	log.info('Starting dbus session service')
	dbus_session = DBusSession(argv)
	dbus_session.dbus_connect()
	dbus_session.start()
	loop = gobject.MainLoop()
	loop.run()

if __name__ == "__main__":
	main(sys.argv)
