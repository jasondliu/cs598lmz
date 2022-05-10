import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
'''

def get_python_file_memory_leak_verification_code(extra_module_imports, extra_body_code):
    return '''
import weakref
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
''' + extra_module_imports + '''
def main():
''' + extra_body_code + '''
while lst:keepali0e.append(lst[:])
main()
'''

def main():
    parser = argparse.ArgumentParser(description='run a command and verify it does not create memory leaks')
    parser.add_argument('command', metavar='COMMAND', type=str, nargs='+',
                       help='the command to run followed by its arguments')
    parser.add_argument('-k','--keepgoing', action='store_true', help='do not stop if a leak is detected')
    parser.add_argument('-l','--leak-threshold', type=int, default=10, help='the maximum number
