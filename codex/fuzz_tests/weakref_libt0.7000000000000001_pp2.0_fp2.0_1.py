import weakref

# modules from other packages

# modules from this package
from .analyses import Analyses, Analysis
from .analysis_factory import AnalysisFactory
from .plots import Plots, Plot
from .session_factory import SessionFactory
from .session_storage import SessionStorage
from .workflow import Workflow

# Load all the registered analyses and plots
from . import analyses
from . import plots


def get_session_factory(**kwargs):
    """Return a session factory to create new sessions."""
    return SessionFactory(**kwargs)


def get_session(file_name, **kwargs):
    """Return a session for the given file name."""
    kwargs.setdefault('format', 'hdf5')
    session_factory = get_session_factory(**kwargs)
    return session_factory(file_name)


def get_analyses(session_factory=None, workflow=None):
    """Return all the available analyses."""
    return Analyses(session_factory, workflow)


def get_analysis(name, session_
