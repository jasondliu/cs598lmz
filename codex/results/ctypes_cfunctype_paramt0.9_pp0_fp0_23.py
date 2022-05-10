import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_bool)
cfunc = FUNTYPE(ctypes.pythonapi.PyThreadState_SetAsyncExc)

from universal_func import *
from progressbar import progress
from math import sqrt, cos, sin, acos
from random import randint, choice


def client_run(client_list, server):
	global thread_messages
	global pygame
	global root
	global os
	global thread_messages_lock
	global clients
	global client_chat_text_list
	global chat_text_list
	global thread_graveyard
	
	init()
	
	running = True
	
	#window = pygame.display.set_mode((640, 480))
	
	while running:
		#events = window.events()
		#events = pygame.event.get()
		events = pygame.event.get()
		
		for event in events:
			if event.type in [pygame.locals.KEYDOWN]:
	
