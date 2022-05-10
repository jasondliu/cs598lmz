import mmap
from random import randint
from fcntl import ioctl


parser = argparse.ArgumentParser()
parser.add_argument('test', choices=['simple-write', 'simple-read'],
                    help='Test type "simpe-write", "simpe-read"')
parser.add_argument('-c', '--count', default=16,
                    help='Number of cycle')
parser.add_argument('--reg', default=0x00,
                    help='Header register')
parser.add_argument('--dout', action='store_true',
                    help='Turn On DOUT trace')
parser.add_argument('--din', action='store_true',
                    help='Turn On DIN trace')
parser.add_argument('--par', action='store_true',
                    help='Turn On PAR trace')
parser.add_argument('--data', action='store_true',
                    help='Turn On DATA trace')
args = parser.parse_args()

# Configuring Simple Trace
tracer = RPISimpleTracer.RPISimpleTracer()
tr
