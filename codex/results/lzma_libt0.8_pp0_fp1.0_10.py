import lzma
lzma.open
lzma.open()

from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('arg1')
parser.add_argument('arg2')
args = parser.parse_args()
args.arg1
args.arg2

from datetime import tzinfo

from datetime import timezone
timezone.utc

from spinfo import p
p.__file__

from spinfo import p
p.__file__

from spinfo.p import mod1
mod1.__file__

from spinfo.p import mod2
mod2.__file__

from spinfo.p.mod1 import func1
func1.__file__

from spinfo.p.mod1 import func2
func2.__file__

from spinfo.p.mod2 import func1
func1.__file__

from spinfo.p.mod2 import func2
func2.__file__

from spinfo.p.mod2 import *
get_foo.__file__

from spinfo.p.mod
