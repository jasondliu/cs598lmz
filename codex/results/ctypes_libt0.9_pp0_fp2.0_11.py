import ctypes
ctypes.cdll.LoadLibrary('bin/glibconfig-2.dll')
ctypes.cdll.LoadLibrary('bin/gconfig-2.dll')
ctypes.cdll.LoadLibrary('bin/gio-2.0-0.dll')
ctypes.cdll.LoadLibrary('bin/pango-1.0-0.dll')
ctypes.cdll.LoadLibrary('bin/png16-16.dll')
ctypes.cdll.LoadLibrary('bin/poppler-22.dll')
ctypes.cdll.LoadLibrary('bin/poppler-glib-8.dll')


import os
this_dir = os.path.dirname(__file__)
project_dir = this_dir

def main():

	'''
	' Объявляем переменную, хранящую в себе переменную, 
	' значение
