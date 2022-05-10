from types import FunctionType
list(FunctionType(lambda x:x,globals()).__globals__.keys())

#6
import inspect
inspect.getfile(inspect.currentframe())

#7
import inspect
inspect.stack()[0][1]

#8
import os
os.path.abspath(__file__)

#9
from __future__ import print_function
print(__file__)

#10
import sys
sys.argv[0]

#11
#第一种
import sys
sys.path[0]
#第二种
import os
os.getcwd()

#12
import os
os.path.dirname(__file__)

#13
import os
os.path.dirname(os.path.abspath(__file__))

#14
import sys
sys.path[0]
import os
os.getcwd()

#15
import sys
print('/'.join(sys.path[0].split('/')[:-1]))


