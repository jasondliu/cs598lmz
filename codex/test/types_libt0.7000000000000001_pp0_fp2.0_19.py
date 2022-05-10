import types
types.SimpleNamespace(a=1, b=2)

# simple_namespace()
def simple_namespace(**dct):
    return types.SimpleNamespace(**dct)
simple_namespace(a=1, b=2)

# is_py2
def is_py2():
    return sys.version_info.major == 2

# is_py3
def is_py3():
    return sys.version_info.major == 3

# is_py36
def is_py36():
    return sys.version_info.major == 3 and sys.version_info.minor >= 6

# is_py37
def is_py37():
    return sys.version_info.major == 3 and sys.version_info.minor >= 7

# is_py38
def is_py38():
    return sys.version_info.major == 3 and sys.version_info.minor >= 8

# is_win
def is_win():
    return sys.platform == 'win32'

# is_linux
