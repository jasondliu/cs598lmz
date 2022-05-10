import weakref

from qtpy.QtCore import Qt, QAbstractItemModel, QModelIndex, QVariant
from qtpy.QtWidgets import QTreeView, QHeaderView

from glue.utils.qt import load_ui
from glue.core.data import Data
from glue.core.data_collection import DataCollection
from glue.core.coordinates import Coordinates
from glue.utils.qt.widget_properties import CurrentComboProperty, CurrentWidgetProperty
from glue.core.message import DataCollectionAddMessage, DataCollectionDeleteMessage
from glue.utils.qt.widget_properties import ValueProperty

__all__ = ["DataCollectionViewer"]


class DataCollectionModel(QAbstractItemModel):

    def __init__(self, dc):
        super(DataCollectionModel, self).__init__()
        self.dc = dc
        self._data = []
        self._data_refs = weakref.WeakValueDictionary()
        self.dc.register_to_hub(self._on_add, DataCollectionAddMessage)
        self.dc.register_to_hub(self
