import ctypes
ctypes.cast(0, ctypes.py_object).value = 'spam'

import sys
sys.path.append('/home/lucas/Área de Trabalho/')
import modulo

print(modulo.soma(10,20))

#-------------------------------------------------------

import modulo as md
print(md.soma(10,20))

#-------------------------------------------------------

from modulo import soma as s
print(s(10,20))

#-------------------------------------------------------

from modulo import *
print(soma(10,20))

#-------------------------------------------------------

import modulo
print(modulo.soma(10,20))

#-------------------------------------------------------

import modulo
print(modulo.soma(10,20))

#-------------------------------------------------------

from modulo import soma
print(soma(10,20))

#-------------------------------------------------------

from modulo import soma as s
print(s(10,20))

#-------------------------------------------------------

from modulo import *
print(soma(10,20))


