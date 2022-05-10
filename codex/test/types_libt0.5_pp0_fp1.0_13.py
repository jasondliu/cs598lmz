import types
types.ModuleType.__repr__ = lambda self: "<module '%s' (%s)>" % (self.__name__, self.__file__)

import os
import sys
import logging
import logging.config
import ConfigParser
import pkg_resources
import pyglet
import pyglet.window
import pyglet.window.key as key
import pyglet.window.mouse as mouse
import pyglet.graphics as graphics
import pyglet.gl as gl
import pyglet.text as text
import pyglet.image as image
import pyglet.sprite as sprite
import pyglet.clock as clock
import pyglet.app as app
import pyglet.event as event
import pyglet.media as media
import pyglet.font as font
import pyglet.window.event as window_event
import pyglet.text.caret as caret
import pyglet.text.layout as layout
import pyglet.text.document as document
import pyglet.text.formats.html as html
import pyglet.text
