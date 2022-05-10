import codecs
# Test codecs.register_error
import pickle
import copyreg
__name__ = 'pickle9'
__package__ = 'pickle9'
class Multi_create_unpickler(pickle.Unpickler):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.dispatch = copyreg.dispatch_table.copy()


class MyObject(object):
	__module__ = 'xxx.xxx'
	def __init__(self, x):
		super().__init__()
		self.x = x

	def __str__(self):
		return f'MyObject(x={self.x!r}, __module__={self.__module__!r})'

MyObject


def create_unpickler(*args, **kwargs):
	return Multi_create_unpickler(*args, **kwargs)
codecs.register_error('strict', codecs.strict_errors)
codecs.register_error('ignore', codecs.ignore_errors)

