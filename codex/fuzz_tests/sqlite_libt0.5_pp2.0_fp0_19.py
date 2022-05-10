import ctypes
import ctypes.util
import threading
import sqlite3
import time

# https://github.com/tito/osxnotifier
# https://github.com/tito/osxnotifier/blob/master/osxnotifier/__init__.py
# https://github.com/tito/osxnotifier/blob/master/osxnotifier/notifier.py
# https://github.com/tito/osxnotifier/blob/master/osxnotifier/notifier.c

# https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man3/objc_msgSend.3.html

# https://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSUserNotification_Class/index.html

# https://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSUserNotification_Class/index.html#//apple_ref/occ/instm/NSUserNotification/setTitle:
# https://develop
