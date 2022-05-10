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
