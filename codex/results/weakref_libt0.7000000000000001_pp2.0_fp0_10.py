import weakref
import logging
logger = logging.getLogger(__name__)

class Backend(object):
    """Abstract base class for all backends.

    The backend processes requests, creates widgets and manages the
    communication between them.

    Parameters
    ----------
    pool : multiprocessing.pool.ThreadPool
        The pool to use for asynchronous tasks.
    """
    _backend_prefix = None
    _backend_version = None

    def __init__(self, pool, **kwargs):
        self._pool = pool
        self._widgets = {}
        self._contexts = weakref.WeakKeyDictionary()

    def widget_for_frontend(self, model):
        """Get a widget for a model.

        This instantiates and caches a widget for the provided model.

        Parameters
        ----------
        model : traitlets.HasTraits
            The model to render

        Returns
        -------
        widget : ipywidgets.Widget
            The widget to use for rendering
        """
        if model.model_id not in self._widgets:

