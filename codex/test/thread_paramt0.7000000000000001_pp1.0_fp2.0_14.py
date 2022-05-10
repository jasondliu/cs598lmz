import sys, threading
threading.Thread(target=lambda: sys.stdin.read()).start()
sys.path.append("/home/pi/Projects/barking_owl/")
from owl import *

ow = Owl()
ow.start_audio()
ow.start_video()

while True:
    ow.get_video()
    ow.get_audio()
    ow.display_video(0)
    ow.display_audio(1)
    ow.display_audio(2)
    ow.display_audio(3)
    ow.display_audio(4)

    ow.update_display()
