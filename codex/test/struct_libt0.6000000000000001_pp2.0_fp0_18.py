import _struct
import threading
import time
import traceback
from PIL import Image
from PIL import ImageDraw
from PIL import ImageEnhance
from PIL import ImageFont
from PIL import ImageOps
from PIL.ExifTags import TAGS
from future.moves import queue

from . import util
from . import vision_constants


class ImageProcessor(threading.Thread):
  """Processes image data from the camera.

  The image processor is responsible for reading the camera, applying
  transforms to the image (such as cropping) and passing the data
  to the vision pipeline.
  """

  def __init__(self, pipeline, camera, camera_config, frame_size=None,
               render_overlay=False):
    """Initialize an ImageProcessor.

    Args:
      pipeline: The vision pipeline.
      camera: The camera.
      camera_config: The camera config.
      frame_size: The size of the output frame or None for full size.
      render_overlay: Set to True to render the overlay.
    """
