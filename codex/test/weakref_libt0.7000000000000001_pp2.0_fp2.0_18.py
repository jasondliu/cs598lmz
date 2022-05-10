import weakref

from gi.repository import Gtk

from kiwi.component import get_utility
from kiwi.datatypes import converter
from kiwi.dist import DistCheck
from kiwi.environ import environ
from kiwi.python import namedany
from kiwi.ui.delegates import Delegate
from kiwi.ui.dialogs import BaseDialog, warning, info, yesno
from kiwi.ui.gadgets import quit_if_last
from kiwi.ui.objectlist import Column
from kiwi.utils import gsignal

from stoqlib.api import api
from stoqlib.database.runtime import get_current_branch, get_current_station
from stoqlib.database.runtime import new_transaction
from stoqlib.database.runtime import Transaction
from stoqlib.domain.interfaces import (IBranch, IPerson, IClient, ICompany,
                                       ISupplier)
from stoqlib.domain.person import Person, Branch
from stoqlib.domain.purchase import PurchaseOrder

