import _struct
import io

try:
    import numpy as N
    numpy_imported = True
except:
    numpy_imported = False

try:
    import PIL
    import PIL.Image
    pil_image_imported = True
except ImportError: 
    pil_image_imported = False

try:
    import Image as pimage
    pyImage_imported = True
except ImportError: 
    pyImage_imported = False

if not pil_image_imported:
    try:
        import image
        image_imported = True
    except ImportError:
        image_imported = False
    
 
#==============================================================================
# PVTtools Exception > PVTtoolsError
#==============================================================================
class PVTtoolsError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

#==============================================================================
# PVTtools > _pt
#============================================================================== 
class _pt:
    
    #--------------------------------------------------------------------------
    #-					
