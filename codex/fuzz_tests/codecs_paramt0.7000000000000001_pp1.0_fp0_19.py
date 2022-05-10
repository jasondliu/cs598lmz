import codecs
codecs.register_error('strict', codecs.ignore_errors)

import pygame
pygame.init()

# Some global variables
screen = None
font = None
mouse = None
mouse_visible = True
mouse_within = False
mouse_pressed = False
mouse_released = False
mouse_moved = False
mouse_dragged = False
mouse_pos = None
button = None
key = None
key_pressed = False
key_released = False
key_mods = None

# We'll use some dictionaries to manage the sets of objects that are currently
# "selected" by various means.
key_selected = {}
mouse_selected = {}
def start_selection_by_key(group, key, **kwargs):
	"""Add a group to the current key selection."""
	key_selected[key] = group
def stop_selection_by_key(key):
	"""Remove a group from the current key selection."""
	del key_selected[key]
def start_selection_by_mouse(group, button, **kwargs):
	"""Add a group to the current mouse selection."""

