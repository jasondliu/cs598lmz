import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
lst[0]=a
del a, callback
import gc; gc.collect()

# Parse arguments
parser = ArgumentParser()
parser.add_argument('--infile', '-i', type=lambda s: open(s), required=True,
                    help='input file (containing the starting weapon set and the set of allowed upgrades)')
parser.add_argument('--outfile', '-o', type=lambda s: open(s, 'w+'), default='-',
                    help='output file (defaults to stdout)')
parser.add_argument('-n', type=int, required=True,
                    help='number of weapon upgrades to find')
parser.add_argument('--seed', type=int, required=True,
                    help='random seed')
parser.add_argument('--max-subsets', type=int, default=0,
                    help='maximum number of subsets to generate, 0 for no limit')
parser.add_argument('--verbose', '-v', action='store_true',
                    help='verbose mode')
parser
