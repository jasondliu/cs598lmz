import bz2
bz2.open
#<classmethod object at 0x7f86d6f08048>
import bz2
bz2.open is open
#True

# 一般来说，上面的方法都是不好的，只有在你真的知道你需要全局访问的情况下才可以使用
# 在本地作用域可以使用内置的 locals 和 globals 函数来访问。例如
import sys
def test():
    return sys.path

# 要访问这个函数中的变量，可以使用
print(test.__globals__['sys'])
#<module 'sys' (built-in)>
print(test.__globals__)
