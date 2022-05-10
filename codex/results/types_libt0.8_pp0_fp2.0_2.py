import types
types.add_method(Button, "get", get)
types.add_method(Button, "set", set)

class Image(viewComponent):
    # Properties
    _path = ""
    _width = 0
    _height = 0
    _left = 0
    _top = 0
    _image = ""

    def get_path(self):
        return self._path
    def set_path(self, path):
        self._path = path
    path = property(get_path, set_path)

    def get_image(self):
        return self._image
    def set_image(self, image):
        self._image = image
    image = property(get_image, set_image)

    def get_width(self):
        return self._width
    def set_width(self, width):
        self._width = width
    width = property(get_width, set_width)

    def get_height(self):
        return self._height
    def set_height(self, height):
        self._height = height
    height = property(get_
