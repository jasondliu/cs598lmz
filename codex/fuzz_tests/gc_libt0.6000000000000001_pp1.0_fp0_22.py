import gc, weakref
import numpy as np

from gwpy.timeseries import TimeSeries
from gwpy.timeseries import TimeSeriesDict
from gwpy.timeseries import StateTimeSeries
from gwpy.time import tconvert
from gwpy.segments import DataQualityFlag, DataQualityDict
from gwpy.segments import Segment, SegmentList
from gwpy.plotter import TimeSeriesPlot
from gwpy.plotter import SegmentPlot
from gwpy.plotter import TablePlot
from gwpy.plot.helpers import (SegmentAxes, SegmentAxesMixin,
                               SegmentAxesFormatter,
                               SegmentAxesLocator)
from gwpy.plot.helpers import (SegmentPlotFormatter,
                               SegmentPlotLocator)

from gwpy.detector import ChannelList
from gwpy.detector.core import Channel
from gwpy.detector import (get_timeseries, get_timeseries_dict)
from gwpy.detector import (get_segments, get_
