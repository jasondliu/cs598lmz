import gc, weakref
from scipy.linalg import toeplitz, inv, pinv

from . import utils


def _noise_psd(y, nfft, nperseg=None, noverlap=None, nfft_bins=None,
               return_onesided=True):
    r"""Compute the noise PSD of a signal `y`.

    Parameters
    ----------
    y : array-like
        Input signal. If `y` is a matrix, the PSD is computed for each
        column.
    nfft : int
        Number of FFT bins.
    nperseg : int or None, optional
        Number of samples to use in each segment. If `nperseg` is ``None``,
        use `nfft` instead.
    noverlap : int, optional
        Number of samples to overlap between segments. If None, ``noverlap =
        nperseg // 2``.
    nfft_bins : array-like or None, optional
        FFT bins to use for computing the noise PSD. If None use all FFT
