import types
types.ModuleType.__file__ = "/private/var/mobile/Library/Preferences/com.apple.springboard.plist"
helpers.ex('import', 'platform')
helpers.ex('import', 'sys')
print sys.modules
print platform.machine()
print sys.getdefaultencoding()
print sys.version_info
print sys.__all__
try:
    print sys.__name__
    print sys.modules.__builtins__
except:
    pass
print sys.maxint
print sys.hexversion
print sys.float_info
try:
    import types
    print types.__name__
except:
    pass
helpers.ex('import', 'os')
print os.sep
print os.sep
print os.name
print os.curdir
helpers.ex('import', 'shutil')
helpers.ex('import', 'socket')
helpers.ex('import', 'ssl')
helpers.ex('import', 'string')
helpers.ex('import', 'struct')
helpers.ex('import', 'subprocess
