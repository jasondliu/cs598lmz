import lzma
lzma.LZMAError

import numpy
numpy.core.multiarray.scalar

import os
os.path.exists

import pygame
pygame.init()
pygame.display.set_mode((1, 1))
pygame.quit()

import pygame.locals
pygame.locals.K_ESCAPE

import pygame.mixer
pygame.mixer.init()
pygame.mixer.music.load('test.ogg')
pygame.mixer.music.play()
pygame.mixer.quit()

import pygame.mixer_music
pygame.mixer_music.load('test.ogg')
pygame.mixer_music.play()

import pygame.sndarray
pygame.sndarray.make_sound(numpy.zeros((1, 1)))

import pygame.surfarray
pygame.surfarray.array3d(pygame.Surface((1, 1)))

import pygame.time
pygame.time.Clock()

import py
