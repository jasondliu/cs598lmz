import weakref


class Renderable(object):
	"""
	A renderable object is an object that is meant to be rendered by the display
	function. It needs to have a rectangle, but in case of complex figures, it
	also needs to have a method called 'render' which will be called from the
	display function.
	"""

	def __init__(self):

		self.rect = pg.rect.Rect(0, 0, 0, 0)
		self._image = None
		self._alpha = 255
		self._visible = True
		self._layer = 0
		self._offset = (0, 0)
		self._angle = 0
		self._scale = (1, 1)
		self._flip = (False, False)

		self.alive = True

	@property
	def layer(self):
		"""The layer of the object, where 0 is low and 100 is high."""
		return self._layer

	@layer.setter
	def layer(self, value):
		self._layer = value

