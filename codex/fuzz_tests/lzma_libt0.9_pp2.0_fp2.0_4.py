import lzma
lzma.open
lzma.decompress
from scipy.misc import imread
from astropy.io import fits
from ccdproc import ccd_process
from photutils.datasets import make_random_kernel
from astropy.stats import gaussian_fwhm_to_sigma
from astropy.convolution import Gaussian2DKernel, Tophat2DKernel, convolve_fft
import logging
from image_registration import chi2_shift
from image_registration.fft_tools import shift


def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

class PhotometryService:

    @staticmethod
    def get_properties_from_fits_file(fits_file, print_properties=False):
        hdu = fits.open(fits_file)
        if print_properties:
            hdu[0].header.ascardlist()['OBJECT'].value
            print(hdu.info())
            hdul
