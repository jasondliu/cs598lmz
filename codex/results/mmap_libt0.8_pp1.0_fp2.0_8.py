import mmap
import sys

# Limit the number of target classes to speed up demo.
MAX_TARGET_CLASSES = 2

class Demo(object):
  """A simple demo which runs object detection on camera frames."""

  def __init__(self, model, labelmap):
    self.model_ = model
    self.labelmap_ = labelmap

    # Initialize session.
    self.sess_ = tf.Session()

  def run(self):
    """Runs inference on a single image.

    Args:
    """
    # Load image.
    image = self.load_image_()
    print(image)
    # Run inference.
    predictions = self.run_inference_on_image_(image)

    # Print the results.
    self.print_results_(predictions, self.labelmap_)

  def load_image_(self):
    """Loads a test image."""
    image = Image.open(sys.argv[1])
    return image

  def run_inference_on_image_(self, image):
    """Runs
