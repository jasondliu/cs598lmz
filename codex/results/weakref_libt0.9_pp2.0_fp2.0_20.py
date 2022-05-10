import weakref

from logging import getLogger


LOG = getLogger(__name__)

imageCache = dict()
class imageControl(QtWidgets.QLabel):   
    """Display an image

    Params:
        pixmap (QPixmap): Display this pixmap
        src (str): Load an image from the file at this path
        db (Database): If present, load image from image table
        imageNum (int): Image number in image table. Only valid with :attr:`db`
        fallback (QPixmap): If pixmap of src cannot be read, display
                            this pixmap
        buttons (bool): Controls whether left click on image brings up
                        a full screen view of the image
        scrollArea (QScrollArea): If present, add image to scroll pane
    """
    def __init__(self, pixmap = None,
                 src = None, 
                 db = None, imageNum = None,
                 corner = False,
                 fallback = QtGui.QPixmap("icons/knot.png"),
                 buttons =
