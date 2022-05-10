import threading
threading._DummyThread._Thread__stop = lambda x: 42

from icecube import icetray, dataclasses, paraboloid, dataio, phys_services, waveform_reco, phys_services, simclasses
from icecube.WaveCalibTools import wave_calib_tools
from icecube.WaveCalibTools.wavedeform import wave_deform

import numpy
import copy
import glob
import os
import sys
import scipy.optimize
import scipy.signal

class WaveformCalibrator(icetray.I3ConditionalModule):
    def __init__(self, context):
        icetray.I3ConditionalModule.__init__(self, context)
        self.AddParameter("WaveformTag", "I3Waveform tag", "OfflinePulses")
        self.AddParameter("CalibrationTag", "I3Calibration tag", "CalibrationInfo")
        self.AddParameter("ReformTag", "I3Calibration tag", "ReformedWaveforms")
        self.AddParameter("ReformWindows", "
