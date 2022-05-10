from types import FunctionType
list(FunctionType("""def __f(a):\n    return a**2""",{},
                   "__f").__globals__.values())[0].__code__.co_freevars

numpy.finfo(float).min

help("modules")

import argparse
help("argparse")


"""
      _            _
     | |          | |
   __| | ___ _ __ | |_
  / _` |/ _ \ '_ \| __|
 | (_| |  __/ | | | |_
  \__,_|\___|_| |_|\__|

"""
import sys
print(sys.path)
# ['', '/Users/beverly/anaconda3/lib/python36.zip',
#  '/Users/beverly/anaconda3/lib/python3.6',
#  '/Users/beverly/anaconda3/lib/python3.6/lib-dynload',
#  '/Users/beverly/anaconda3/lib/python3.6/site-packages
