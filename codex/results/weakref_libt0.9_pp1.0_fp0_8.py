import weakref
import os

from numpy import log10
from xml.etree import ElementTree

from orangecontrib.wonder.controller.fit.fit_parameter import ParametersList
from orangecontrib.wonder.controller.fit.fit_parameter import FitParameter
from orangecontrib.wonder.controller.fit.fit_global_parameters import GlobalParameters


class FitGlobalSettings(object):

    class Slice(object):

        def __init__(self, start, width, stop):
            self.start = start
            self.width = width
            self.stop = stop

            if self.start is not None:
                if self.width is not None:
                    self.stop = self.start + self.width
                else:
                    self.width = self.stop - self.start
            elif self.stop is not None:
                if self.width is not None:
                    self.start = self.stop - self.width
                else:
                    self.width = self.stop - self.start
            elif self.width is not None:
                if self.start is
