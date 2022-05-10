import gc, weakref

from affine import Affine
from rasterio.enums import MaskFlags

from rasterio._err import CPLE_AppDefined, CPLE_OutOfMemory

def geom_window(geom, fwd, inv, boundary=1, intersects=False):
    """Return an affine transform, width and height for window containing
    a geometry.

    Parameters
    ----------
    geom: shapely.geometry
        A geom or MultiGeom to be contained in the window.
    fwd: rasterio.Affine
        Affine transform used to convert geometries to pixel coordinates.
    inv: rasterio.Affine
        Affine transform used to convert pixels to geom coordinates.
    boundary: int
        Number of pixels to include in the window boundary.
    intersects: bool
        Return window containing the intersection of geom and bounds.
        Use to clip a geom to a window.

    Returns
    -------
    t: rasterio.Affine
        Affine transform for the new window.
    width: int
        Width of the new window
