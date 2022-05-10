import ctypes
import ctypes.util
import threading
import sqlite3
import os
import subprocess
import sys
import time

# OS X specific imports
import objc
from Foundation import *
from AppKit import *
from PyObjCTools import AppHelper

# OS X AppKit constants
kCFUserNotificationAlertHeaderKey = "AlertHeader"
kCFUserNotificationAlertMessageKey = "AlertMessage"
kCFUserNotificationAlternateButtonTitleKey = "AlternateButtonTitle"
kCFUserNotificationDefaultButtonTitleKey = "DefaultButtonTitle"
kCFUserNotificationIconURLKey = "IconURL"
kCFUserNotificationSoundURLKey = "SoundURL"
kCFUserNotificationTextFieldTitlesKey = "TextFieldTitles"
kCFUserNotificationTextFieldValuesKey = "TextFieldValues"

# OS X AppKit constants
kCFUserNotificationDefaultResponse = 0
kCFUserNotificationAlternateResponse = 1
kCFUserNotificationOtherResponse = 2
kCFUserNotificationCancelResponse = 3

# OS X AppKit constants
kCFUserNotificationNoDefaultButtonFlag = (1 << 5)
kCFUserNot
