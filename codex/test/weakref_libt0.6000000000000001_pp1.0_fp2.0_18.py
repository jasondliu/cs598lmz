import weakref

import gtk
import gobject

from kiwi.datatypes import currency
from kiwi.ui.dialogs import yesno
from kiwi.ui.objectlist import Column
from kiwi.ui.widgets.contextmenu import ContextMenu
from kiwi.ui.widgets.button import Button

from stoqlib.api import api
from stoqlib.domain.payment.payment import Payment
from stoqlib.domain.payment.views import InPaymentView, OutPaymentView
from stoqlib.domain.person import Branch
from stoqlib.gui.base.dialogs import run_dialog
from stoqlib.gui.base.dialogs import get_current_toplevel
from stoqlib.gui.dialogs.paymentchangedialog import (PaymentChangeDialog,
                                                     PaymentChangeMethodDialog)
from stoqlib.gui.dialogs.salesquotedialog import QuoteDetailsDialog
from stoqlib.gui.editors.noteeditor import NoteEditor
from stoqlib.gui.search.personsearch import ClientSearch
