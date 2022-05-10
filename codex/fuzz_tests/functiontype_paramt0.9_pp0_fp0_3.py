from types import FunctionType
list(FunctionType([1], lambda: 0, {}, None))

class Ret(Exception): pass
def ret(): raise Ret()

class A(object):
	def __len__(self): ret()

z = []
try:
	z[...]
except Ret:
	pass

try:
	z[..., 0]
except Ret:
	pass

try:
	z[0, ...]
except Ret:
	pass

try:
	z[0, ..., 1]
except Ret:
	pass

class B(A):
	def __getitem__(self, index): ret()

z = B()
try:
	z[...]
except Ret:
	pass

try:
	z[..., 0]
except Ret:
	pass

try:
	z[0, ..., 1]
except Ret:
	pass

z = [1]
try:
	z[..., 0]
except ValueError:
	pass

try:
	z[0, ..., 1]
except ValueError:
	pass

class
