import _struct
import time
import traceback
import pygame
from threading import Thread,RLock
import sys

from threading import Thread,RLock

lock = RLock()

def send(msg):
    lock.acquire()

    try:
        sock.send(msg)
    except Exception, e:
        print('a problem occurred while sending data:', e)

    lock.release()

def recv():
    lock.acquire()

    try:
        data = sock.recv(4096)
    except Exception, e:
        print('a problem occurred while receiving data:', e)

    lock.release()

    return data

def main(s):
    global sock

    width = 1080
    height = 710
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("V_Ball")
    clock = pygame.time.Clock()

    background = pygame.image.load("court.jpg")
    font = pygame.font.SysFont("comics
