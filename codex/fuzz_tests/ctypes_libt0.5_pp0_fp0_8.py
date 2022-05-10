import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Elevator Simulator")

#importing libraries
import pygame as pg
from pygame.locals import *
import sys, os, random, math, time

#initializing pygame
pg.init()

#setting up the window
pg.display.set_caption("Elevator Simulator")
screen = pg.display.set_mode((800, 600))

#setting up the clock
clock = pg.time.Clock()

#setting up the fonts
pg.font.init()
mainFont = pg.font.SysFont('Comic Sans MS', 30)

#loading in the images
bg = pg.image.load("images/bg.png")

#defining some colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#defining some variables
floor = 0
floorPos = [0, 0, 0, 0, 0]
floorButton = [
