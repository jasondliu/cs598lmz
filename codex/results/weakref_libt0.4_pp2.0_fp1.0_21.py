import weakref

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

from . import config
from . import log
from . import util
from . import worker
from . import worker_pool
from . import worker_pool_manager

logger = log.get_logger(__name__)


class WorkerPoolManager(QObject):
    """
    Manages a pool of workers.
    """

    # Signals
    #
    # Emitted when the worker pool is updated.
    #
    # Parameters:
    #   worker_pool (worker_pool.WorkerPool): The worker pool.
    worker_pool_updated = pyqtSignal(worker_pool.WorkerPool)

    # Emitted when the worker pool manager is finished.
    #
    # Parameters:
    #   worker_pool_manager (worker_pool_manager.WorkerPoolManager): The worker
    #     pool manager.
    finished = pyqtSignal(worker_pool_manager.WorkerPoolManager)

    def __init__(self,
                 worker_pool
