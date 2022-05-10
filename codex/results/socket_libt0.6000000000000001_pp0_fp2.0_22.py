import socket
import sys
import time
import threading
import random
import pygame
from pygame.locals import *
import pygame.font
from pygame.locals import *
from socket import error as SocketError
import errno
import os

# X_AXIS = 0
# Y_AXIS = 1

# pygame.font.init()
# font = pygame.font.Font(None, 40)
# text = font.render('Hello world', 1, (255,255,255))
# textpos = text.get_rect()
# textpos.centerx = screen.get_rect().centerx
# screen.blit(text, textpos)
# pygame.display.update()

# pygame.init()
# pygame.display.set_mode( (400, 300) )

# def sendData(s):
#     while True:
#         msg = input(">> ")
#         s.send(msg.encode("utf8"))
#         if msg == "{quit}":
#             s.close()
#             break

#
