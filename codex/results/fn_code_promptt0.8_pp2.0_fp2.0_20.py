fn = lambda: None
# Test fn.__code__
try:
	fn.__code__
except AttributeError:
	pass
else:
	raise TestFailed('lambda fn.__code_ attribute should not exist')
# Test fn.__globals__
try:
	fn.__globals__
except AttributeError:
	pass
else:
	raise TestFailed('lambda fn.__globals__ attribute should not exist')

# Test __new__.  SF bug 1354106.
import UserList

# Old-style class
class CustomUserList(UserList.UserList):
	def __new__(cls):
		return []

# New-style class
class NewStyleClass(object):
	def __new__(cls):
		return []

try:
	CustomUserList()
except TypeError:
	pass
else:
	raise TestFailed('__new__ method in CustomUserList should fail')

try:
	NewStyleClass()
except TypeError:
	pass
else:
	raise TestFailed('__new__ method in NewStyleClass should fail')
