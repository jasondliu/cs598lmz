import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

from pygame import mixer # Load the required library

mixer.init()
mixer.music.load('/home/pi/Music/music.mp3')
mixer.music.play()

from time import sleep
sleep(10)

mixer.music.stop()
