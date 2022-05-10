import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('Agora você escuta?')
