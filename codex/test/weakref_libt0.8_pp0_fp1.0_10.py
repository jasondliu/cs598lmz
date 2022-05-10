import weakref

from pydbus import SessionBus
from PyQt5.QtCore import QObject, pyqtSlot, QTimer

_logger = logging.getLogger(__name__)

try:
    from typing import Any, Optional, Callable, List, Tuple
except ImportError:
    pass


class QIndicator(QObject):
    """Indicator Model"""

    def __init__(self, name: str,
                 get_menu: Callable[[], List[Tuple[str, str]]]) -> None:
        """Indicator Model

        Args:
            name (str): Indicator name.
            get_menu (Callable[[], List[Tuple[str, str]]]):
                Function that returns menu items.
        """
        super().__init__()

        self._calls: List[Any] = []
        self._timer: Optional[QTimer] = None

