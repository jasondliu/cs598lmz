import weakref

import numpy as np

from .. import registry
from ..util import log
from ..util.config import Config
from ..util.fit import fit, fit_graph
from ..util.liveplot import LivePlot
from ..util.stats import cdf_fit
from . import analysis, extract, plot

logger = log.get_logger(__name__)


class Dummy:
    pass


class Analysis(analysis.AnalysisBase):
    """
    Analysis for a single device.
    """

    def __init__(self, config, data=None):
        """
        Create a new Analysis.

        Parameters
        ----------
        config : dict or :class:`~.util.config.Config`
            Configuration for this analysis.
        data : dict, optional
            Analysis data.
        """
        super().__init__(config, data)
        if data is not None:
            self.data = data
        else:
            self.data = {}

        self.data['fluence'] = None
        self.data['n_doses'] = None
        self
