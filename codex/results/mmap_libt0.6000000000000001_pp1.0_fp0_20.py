import mmap
import struct

from ctypes import *
from sdl2 import *

import pygame.image
import pygame.display
import pygame.transform

import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont


def main():
    SDL_Init(SDL_INIT_VIDEO)

    win = SDL_CreateWindow(b"Hello",
                           SDL_WINDOWPOS_CENTERED,
                           SDL_WINDOWPOS_CENTERED,
                           800, 600,
                           SDL_WINDOW_SHOWN)

    winSurf = SDL_GetWindowSurface(win)
    winPix = cast(winSurf.contents.pixels, POINTER(c_uint32))

    # Create surface
    surf = SDL_CreateRGBSurface(0, 800, 600, 32,
                                0x000000ff,
                                0x0000ff00,
                                0x00ff0000,
                                0xff000000)

    surfPix = cast(surf.contents.pixels, POINTER(c_uint
