import gc, weakref
import logging

from kiwi.datatypes import ValidationError
from kiwi.environ import environ
from kiwi.ui.objectlist import ObjectTree, ObjectList
from kiwi.ui.dialogs import warning
from kiwi.ui.views import BaseView
from kiwi.utils import gsignal, type_register

from stoqlib.database.orm import AND
from stoqlib.database.runtime import get_connection, new_transaction
from stoqlib.domain.interfaces import IStorable
from stoqlib.domain.product import Product
from stoqlib.domain.transfer import TransferOrderItem
from stoqlib.gui.base.search import SearchEditor
from stoqlib.gui.base.dialogs import run_dialog
from stoqlib.gui.base.lists import SearchResultListSlave
from stoqlib.gui.editors.baseeditor import BaseEditor
from stoqlib.gui.editors.inventoryeditor import InventoryEditor
from stoqlib.gui.editors.noteeditor import NoteEditor
from stoqlib.gui.
