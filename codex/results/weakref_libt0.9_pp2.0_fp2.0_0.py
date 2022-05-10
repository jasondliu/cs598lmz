import weakref

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')

from gi.repository import Gtk
from gi.repository import Gdk

import louie as dispatcher

from .base import BasePage, PageName, PageOrder
from .assistant import WolfPackAssistant, COMPONENT_MODE_ADVANCED
from .task import WolfTask

from ....config import Config
from ....core.beamline import Beamline
from ....core.utils import JsonSerializable

from ...newwizards import wizardpages

from ....core.instrument.instrument import Instrument

#setup logging
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)


class InstrumentConfigWizard(WolfPackAssistant):

    def __init__(self, instrument, *args, **kwargs):
        WolfPackAssistant.__init__(self, *args, **kwargs)
        self.set_title("Create Instrument")
        self.get
