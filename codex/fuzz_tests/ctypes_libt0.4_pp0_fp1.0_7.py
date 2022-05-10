import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import subprocess
subprocess.Popen(['start', 'alarm.mp3'], shell=True)

import pygame
pygame.init()
pygame.mixer.music.load("alarm.mp3")
pygame.mixer.music.play()

import time
time.sleep(10)

import pygame
pygame.mixer.music.stop()
