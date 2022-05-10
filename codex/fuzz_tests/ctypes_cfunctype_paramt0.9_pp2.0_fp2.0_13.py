import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_float)

class ESMF(object):
    '''ESMF interface (only lon-lat grid and nearest neighbor approx are implemented yet)'''
    def __init__(self, lon, lat):
        self._setup_mesh(lon, lat)

    def _setup_mesh(self, lon, lat):
        self.lon = lon
        self.lat = lat
        if self.lon.shape != self.lat.shape:
            raise Exception('Number of lat and lon points must be the same')
        if self.lon.shape[0] < self.lon.shape[1]:
            fmt = 'Grid must have 1st dimension as lat, 2nd as lon'
            raise Exception(fmt)
        self.shape = tuple(reversed(self.lon.shape))

        lib = ctypes.cdll.LoadLibrary(ESMF.lib_name)
        mesh = lib.ESMF_MeshCreate(np.prod(self.shape), 0, ['ESMC_COORDINATE_LON', 'ESMC_
