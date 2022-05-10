import weakref
import threading

from gi.repository import GObject, Gtk

from ..ui import BuilderWidget
from . import (
    RuntimeErrorDialog,
    RuntimeWarningDialog,
    RuntimeInfoDialog,
    RuntimeChoiceDialog,
    RuntimeInputDialog,
    RuntimePasswordDialog,
)


class App:

    def __init__(self, app_id, app_name, app_description, app_version,
                 app_copyright, app_website, app_license, app_authors,
                 app_logo, app_icon, app_documenters, app_artists):
        self.id = app_id
        self.name = app_name
        self.description = app_description
        self.version = app_version
        self.copyright = app_copyright
        self.website = app_website
        self.license = app_license
        self.authors = app_authors
        self.logo = app_logo
        self.icon = app_icon
        self.documenters = app_documenters
        self.artists =
