import types
# Test types.FunctionType
assert( isinstance( types.FunctionType, type ) )
assert( issubclass( types.FunctionType, object ) )
# Test types.LambdaType
assert( isinstance( types.LambdaType, type ) )
assert( issubclass( types.LambdaType, object ) )
# Test types.GeneratorType
assert( isinstance( types.GeneratorType, type ) )
assert( issubclass( types.GeneratorType, object ) )

def func( a, b ):
    return a+b
# Enables reloading after changes to this module
from imp import reload
import instanceof_iface_usercode
reload( instanceof_iface_usercode )
# Test usercode.UserClass
assert( isinstance( instanceof_iface_usercode.UserClass(), object ) )

from wxPython import wx
app = wx.App()
# Test wx.CommandEvent
assert( isinstance( wx.CommandEvent(), object ) )
from UserList import UserList
# Test UserList.UserList
assert( isinstance(
