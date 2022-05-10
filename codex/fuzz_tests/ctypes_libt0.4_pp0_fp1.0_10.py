import ctypes
ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)

#import winsound
#winsound.MessageBeep()

#import os
#os.system("echo 'Hello world!' | festival --tts")

#from win32com.client import Dispatch
#speak = Dispatch("SAPI.SpVoice")
#speak.Speak("Hello World")

from playsound import playsound
playsound('C:\\Users\\User\\Desktop\\sound.mp3')
