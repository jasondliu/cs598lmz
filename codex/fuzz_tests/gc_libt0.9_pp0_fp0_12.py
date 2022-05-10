import gc, weakref
    >>> import pyfits
    >>> import pywcs
    >>> f = pyfits.open('test0.fits')
    >>> w = pywcs.WCS(f[0].header)
    >>> l = []
    >>> for j in xrange(500):
    ...     l.append(weakref.ref(w.wcs_pix2world(10., 10., 0)))
    ...
    >>> del w
    >>> gc.collect()
    0
    >>> for ref in l:
    ...     if ref() is not None:
    ...         k += 1
    >>> k

    """
    return _prj2_wrap('cf_cp2w', input, output, ph0, nl, **kwargs)

#------------------------------------------------------------

def cpb2s(input, output, phi, **kwargs):
    """
    Cartesian to spherical projection:

    .. math::

       \\xi = \\rho \\sin \\theta\\cos \\phi

    """
    return _prj2_wrap('cf_cpb2s', input, output, phi,
