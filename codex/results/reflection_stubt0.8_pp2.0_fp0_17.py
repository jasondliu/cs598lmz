fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_flags = 666

try:
    fn()
except ValueError:
    print('ERROR')
else:
    print('END')
EOF

pyver=$(python -V 2>&1 | sed -e 's/Python \([0-9.]*\).*/\1/')

echo
echo
echo "python $pyver with version_info >= (3,3)"
case "$pyver" in
    3.1|3.2) exit 0;;
esac

python <<EOF
import sys

if sys.version_info < (3,3):
    exit(1)

class A:
    def __init__(self):
        self.x = None
        self.y = 47
        self.z = None
        self.w = None
        self.a = 47

a = A()

def get_y(self):
    return self.y

def get_z(self):
    raise ValueError("not implemented")

def get_w(self):
