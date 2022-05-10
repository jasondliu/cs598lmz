import weakref

from util.accelerator import set_accelerator
# from util.settings import Settings
# from views.builder import Builder
from .consts import *
from .generator import Generator

class Gui(Gtk.Application):

    def __init__(self, name, id, version, comment, icon_name, author,
                 email, website, copyr, license, translator, command, args):
        # Private
        self.name = name # fumon
        self.id = id # com.github.rastersoft.fumon
        self.version = version
        self.comment = comment
        self.icon_name = icon_name
        self.author = author
        self.email = email
        self.website = website
        self.copyr = copyr
        self.license = license
        self.translator = translator
        self.command = command
        self.args = args
        self.window = None
        self.settings = None
        self.builder = None
        self.generator = None
        self.own_config = None
        self
