import threading
threading.stack_size(2 * 1024 * 1024)

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from imutils import paths
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt

import time
import sys

## pygame imports
import pygame
from pygame.locals import *
from OpenGL.GL import glLoadIdentity
from OpenGL.GL import glTranslatef, glRotatef
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL import shaders

## Kivy imports
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.graphics import Color, Line, Rectangle
from kivy.graphics
