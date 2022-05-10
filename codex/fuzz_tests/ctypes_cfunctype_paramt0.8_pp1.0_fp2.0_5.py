import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def gauss(nx, ny, xmin, xmax, ymin, ymax, m, s):
    """
    Returns a 2D Gaussian distribution with
    mean m and dispersion s

    Parameters
    ----------
    nx : int
        number of points along x
    ny : int
        number of points along y
    xmin : float
        minimum x
    xmax : float
        maximum x
    ymin : float
        minimum y
    ymax : float
        maximum y
    m : array
        mean
    s : array
        dispersion

    Returns
    -------
    data : array
        2D Gaussian distribution
    """

    dx = (xmax-xmin)/(nx-1)
    dy = (ymax-ymin)/(ny-1)

    def gauss_y(x,y):
        """
        Returns normalized Gaussian along y

        Parameters
        ----------
        x : float
            x value where to
