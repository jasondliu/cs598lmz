import weakref

import numpy as np

from phy.utils.collections import Bunch
from phy.utils.contextmanagers import ignored
from phy.utils.logging import logger
from .base import (
    ClusterMetric, ClusterMetrics, ClusterView, ClusterViews, Controller, GUI, FeatureView, ScatterView)
from .kwik_accessor import KwikAccessor
from .kwik_model import KwikModel
from .views import WaveformsView, FeaturesView, TracesView, TraceView, AutocorrelogramsView, \
    CrosscorrelogramsView, CorrelogramsView, IsiHistogramsView, ScatterView, AmplitudeView, \
    FeatureCorrelogramsView, MetricsView, ModelView, CorrelogramsByClusterView, \
    ClusterContaminationView, ClusterAmplitudesView


def show_gui(info, filename, **kwargs):
    cluster_metrics = ClusterMetrics(info)
    controller = Controller(
        model=KwikModel(filename, **kwargs),
        views=[
            View(cluster_metrics),

