import weakref
import sys
from collections import OrderedDict
from dtcwt.coeffs import qshift
from dtcwt.numpy.lowlevel import colfilter as np_colfilter, coldfilt as np_coldfilt
from dtcwt.opencl.lowlevel import coldfilt as cl_coldfilt
from dtcwt.opencl.lowlevel import colfilter as cl_colfilter
from dtcwt.opencl.lowlevel import coldfilt_plan
from dtcwt.opencl.lowlevel import colfilter_plan
from dtcwt.opencl.lowlevel import colfilter_prepare_reals_plan
from dtcwt.opencl.lowlevel import colfilter_prepare_reals
from dtcwt.opencl.lowlevel import colfilter_prepare_reals_inplace
from dtcwt.opencl.lowlevel import colfilter_prepare_reals_inplace_plan
from dtcwt.opencl.lowlevel import colfilter_reconstruct_reals
from dtcwt.opencl.lowlevel import colfilter_re
