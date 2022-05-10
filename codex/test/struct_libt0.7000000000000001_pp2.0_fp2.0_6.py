import _struct
import _globals

def _set_key_modifiers(event):
	""" Set the _globals._key_modifiers global variable """
	
	_globals._key_modifiers = event.modifiers
	
def _set_mouse_modifiers(event):
	""" Set the _globals._mouse_modifiers global variable """
	
	_globals._mouse_modifiers = event.modifiers
	
def _set_mouse_position(event):
	""" Set the _globals._mouse_position global variable """
	
	_globals._mouse_position = event.pos
	
def _set_mouse_buttons(event):
	""" Set the _globals._mouse_buttons global variable """
	
	_globals._mouse_buttons = event.buttons
	
def _get_key_modifiers():
	""" Returns the current _globals._key_modifiers variable """
	
	return _globals._key_modifiers
	
