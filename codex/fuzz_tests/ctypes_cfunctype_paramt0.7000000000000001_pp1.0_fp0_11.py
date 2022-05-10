import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

import numpy as np
from numpy import ctypeslib
from numpy.testing import (
    assert_, assert_raises, assert_equal, assert_allclose
)
from numpy.fft import (
    fft, ifft, fft2, ifft2, fftn, ifftn, rfft, irfft, fftshift, ifftshift,
    fftfreq, rfftfreq, fft2, ifft2, fftn, ifftn, hfft, ihfft, hfft2,
    ihfft2, hfftn, ihfftn, rfft2, irfft2, rfftn, irfftn, dct, idct, dctn,
    idctn, dst, idst, dstn, idstn, dctn, idctn, dst, idst, dstn, idstn,
    fftwnd_n_byte_align_empty, fftwnd_n_byte
