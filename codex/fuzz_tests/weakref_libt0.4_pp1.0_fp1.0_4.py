import weakref

from gi.repository import Gtk
from gi.repository import Gdk

from kiwi.ui.delegates import Delegate
from kiwi.ui.objectlist import Column, ObjectTree
from kiwi.utils import gsignal

from stoqlib.api import api
from stoqlib.domain.person import Branch
from stoqlib.domain.product import Product, ProductStockItem
from stoqlib.domain.stock import StockTransactionHistory
from stoqlib.gui.base.dialogs import run_dialog
from stoqlib.gui.base.lists import ModelListDialog
from stoqlib.gui.base.search import SearchEditor
from stoqlib.gui.dialogs.productstockdetails import ProductStockHistoryDialog
from stoqlib.gui.editors.baseeditor import BaseEditor
from stoqlib.gui.editors.producteditor import ProductStockEditor
from stoqlib.gui.search.productsearch import ProductStockSearch
from stoqlib.gui.search.searchcolumns import SearchColumn, QuantityColumn
from stoqlib.gui.slaves
