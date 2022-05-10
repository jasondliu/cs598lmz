import ctypes
ctypes.cdll.LoadLibrary('./face_recognition/lib/libflandmark_detector.so')

from . import libflandmark_detector
from .libflandmark_detector import (
    FLANDMARK_Model,
    FLANDMARK_Data,
    flandmark_init,
    flandmark_detect)


FLANDMARK_DAT = os.path.abspath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "data",
    "flandmark_model.dat")
)


class Flandmark:

    """
    Flann based detector.

    Parameters
    ----------
    detect_multiple_faces: bool, optional
        If true then multiple faces will be detected.

    Returns
    -------
    :class:`zunis.models.flandmark.DetectMultipleFaces`
        Child class with method `return_landmarks` if
        `detect_multiple_faces=True`.


    Attributes
    ----------
    detector
