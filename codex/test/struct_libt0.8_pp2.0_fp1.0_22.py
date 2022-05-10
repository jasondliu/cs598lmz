import _struct
import gc
import sys
import unittest
from test import support
from sys import getrefcount as grc
from _testcapi import INT_MAX, INT_MIN
from _testcapi import getargs_b, getargs_B, getargs_h, getargs_H
from _testcapi import getargs_i, getargs_I, getargs_k, getargs_K
from _testcapi import getargs_l, getargs_L, getargs_n, getargs_N
from _testcapi import getargs_q, getargs_Q, getargs_e, getargs_f
from _testcapi import getargs_d, getargs_s, getargs_p, getargs_P
from _testcapi import getargs_c, getargs_u, getargs_S, getargs_Z
from _testcapi import getargs_C, getargs_O, getargs_Y, getargs_U, getargs_V
from _testcapi import getargs_y_z, getargs_y_z_i
