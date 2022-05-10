import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\a')).start()

import os
os.system("echo -n '\a'")

import winsound
winsound.Beep(1000, 500)

import winsound
winsound.MessageBeep(winsound.MB_ICONASTERISK)

import winsound
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

import winsound
winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

import winsound
winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)

import winsound
winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)

import winsound
winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

import winsound
winsound.PlaySound("SystemDefault", winsound.SND_ALIAS)

import winsound
winsound.PlaySound("SystemStart", winsound.SND_ALIAS)

import
