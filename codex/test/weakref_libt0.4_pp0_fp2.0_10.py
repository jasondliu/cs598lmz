import weakref

import gtk
import gobject

from kiwi.component import get_utility
from kiwi.datatypes import ValidationError
from kiwi.ui.delegates import Delegate
from kiwi.ui.gadgets import quit_if_last
from kiwi.ui.objectlist import Column
from kiwi.ui.widgets.contextmenu import ContextMenu
from kiwi.utils import gsignal

from stoqlib.api import api
from stoqlib.domain.person import Branch
from stoqlib.domain.transfer import TransferOrder
from stoqlib.gui.base.dialogs import run_dialog
from stoqlib.gui.base.lists import ModelListDialog
from stoqlib.gui.dialogs.transferorderdialog import TransferOrderDetailsDialog
from stoqlib.gui.editors.baseeditor import BaseEditor
from stoqlib.gui.editors.transfereditor import TransferOrderEditor
from stoqlib.gui.utils.printing import print_report
