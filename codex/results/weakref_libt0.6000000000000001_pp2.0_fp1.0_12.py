import weakref

import numpy as np

from pynwb.base import TimeSeries, NWBDataInterface
from pynwb.ophys import TwoPhotonSeries, OpticalChannel
from pynwb.form.backends.hdf5 import HDF5IO
from pynwb.form.backends.hdf5.h5_utils import H5DataIO

from .base import _BaseMixin
from .base import _create_device, _create_optical_channel, _create_electrical_series
from .time_series import _add_time_series, _add_dynamic_table
from .time_series import _add_spatial_series, _add_image_series
from .time_series import _add_electrical_series
from .time_series import _add_roi_response_series
from .time_series import _add_roi_table_region
from .time_series import _add_roi_table_region_list
from .time_series import _add_image_segmentation
from .time_series import _add_image_segmentation_mask

