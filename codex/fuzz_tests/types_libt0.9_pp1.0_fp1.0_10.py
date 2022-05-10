import types
types.UnicodeType = types.StringType

import exceptions
RuntimeError = exceptions.RuntimeError

import sys
PY_NAME = '/usr/lib/python2.5/'

sys.path.append(PY_NAME)
sys.path.append(PY_NAME + 'site-packages')
#sys.path.append(PY_NAME + 'lib-dynload')
#sys.path.append(PY_NAME + 'plat-sunos5')

import os
if 'RESOURCE_PATH' in os.environ:
    sys.path.append(os.environ['RESOURCE_PATH'])
sys.path.append('./')

import pygame
print 'PYTHON VERSION:', sys.version
print 'PYGAME VERSION:', pygame.version.ver


font_size = 30
font_color = (255, 255, 255)
button_color = (117, 158, 202)


def show_error(msg):

    text = pygame.font.SysFont('bitstreamverasans', font_
