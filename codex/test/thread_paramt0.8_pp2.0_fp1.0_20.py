import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\a'))
 
# beep
sys.stdout.write('\a')
sys.stdout.flush()
 
# play a wave file
import winsound
winsound.PlaySound('train.wav', winsound.SND_FILENAME)

# winsound.MessageBeep()

# ビープ音を鳴らす
# import winsound
# duration = 1000  # millisecond
# freq = 440  # Hz
# winsound.Beep(freq, duration)

# import subprocess
# subprocess.call(["afplay", "sound.wav"])

# from __future__ import print_function
# import os
# print('\a', end='')
# os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (1, 1000))
