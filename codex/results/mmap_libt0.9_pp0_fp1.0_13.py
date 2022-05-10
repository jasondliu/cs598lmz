import mmap
import os

from pyro3d import IModel


class Model(IModel):
    def get_name(self):
        return "pyro-bin"

    def is_supported(self, filename):
        return filename.endswith(".bin")

    def map_texture_coordinates(self):
        return True

    def is_streamable(self):
        return True

    def is_double_sided(self):
        return True

    def supports_colors(self):
        return True

    def supports_morph_targets(self):
        return True

    def __init__(self, filename, buffersize=1024 * 1024, animated=False):
        IModel.__init__(self, filename)
        self.mm = mmap.mmap(fd=open(filename, "rb", buffering=buffersize).fileno(),
                            length=os.path.getsize(filename), access=mmap.ACCESS_READ)
        self.animated = animated

        count = self.mm[:4].unpack(">i")[
