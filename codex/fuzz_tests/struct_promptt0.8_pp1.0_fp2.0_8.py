import _struct
# Test _struct.Struct with all possible sizes, formats and alignments.
import string
import random
import sys

# Choose one of the following lines depending on how you want to test the
# module:

# Testing against C code compiled with gcc -O2 -fPIC -shared -static-libgcc:
# from _struct_gcc_test import *

# Testing against C code compiled with an MSVC DLL.
# from _struct_msvc_test import *

# Testing against C code compiled with gcc -O2 -shared -fPIC:
# from _struct_pic_test import *

# Testing against C code compiled with gcc -O2 -shared:
# from _struct_no_pic_test import *

# Testing against a Python module containing the C code:
# from _struct_c_code import *

# Testing against a Python module containing the C code, compiled with
# --with-pydebug:
# from _struct_c_code_g import *

# Testing against a Python module containing the C code, compiled with
# PY_NO_SHORT_FLOAT_
