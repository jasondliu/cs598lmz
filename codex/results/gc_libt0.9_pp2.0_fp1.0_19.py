import gc, weakref
import inspect

##################################################################################################################################
### Base Class for descriptor variables
##################################################################################################################################

class abstract_descriptor(object):
	"""Abstract base class for descriptor variables.
	Classes subclassing abstract_descriptor should be used as a decorator of the functions they decorate.
	Eg:

	class my_descriptor_variable(abstract_descriptor):
		...

	@my_descriptor_variable
	def my_function(self, ...):
		...

	EXAMPLE USAGE:
	-------------
	>>> class my_descriptor_variable(abstract_descriptor):
	...	global_attributes = ['foo'] # Runs every function
	...	class_attributes = ['bar'] # Runs every function of a 'bar' class instance
	...	attributes = ['stuff'] # Runs every function of a 'stuff' instance
	...	def initialize_global(self, **kwargs):
	...		globals()['foo'] = 'baz'
	...	def initialize_class(self, **kw
