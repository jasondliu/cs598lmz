import _struct
import zlib
from colorsys import hsv_to_rgb
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Loader:
	def loadfile(self, fn):
		with open(fn, "rb") as f:
			self.data = f.read()

	def loaddata(self, data):
		self.data = data


class ImageLoader(Loader):
	def __init__(self, *args, **kwargs):
		self.data = None

	def is_png(self):
		try:
			im = Image.open(BytesIO(self.data))
			im.load()
			width, height = im.size
			return True
		except IOError:
			pass
			return False


class FontLoader(Loader):
	def __init__(self, *args, **kwargs):
		self.data = None

