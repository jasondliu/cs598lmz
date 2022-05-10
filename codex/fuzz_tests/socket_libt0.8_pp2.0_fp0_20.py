import socket
import threading
import random
import pickle
import sys
import os

"""
	Recursión ahora
"""

"""
	Clase para la caja de la cual el cliente puede cambiar todos sus parámetros
	(la que envía al servidor)
"""
class Caja:
	"""
		Constructor de la clase
	"""
	def __init__(self, x = 0, y = 0, h = 0, w = 0, r = 0, g = 0, b = 0):
		self.x = x
		self.y = y
		self.h = h
		self.w = w
		self.r = r
		self.g = g
		self.b = b
	
	"""
		Suma entre dos cajas
	"""
	def __add__(self, otro):
		return Caja(self.x + otro.x, self.y + otro.y, self.h + otro.h, self.
