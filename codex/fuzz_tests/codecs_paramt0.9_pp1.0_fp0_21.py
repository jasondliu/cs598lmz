import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import _measurement as mp #nested module


def makeSub(name, value, type=None, unit=None, parent=None):
    if type is not None:
        value=type(value)
    if unit is not None:
        value=value.withUnit(unit)
    s=mp.Sub(name, value, parent=parent) 
    return s

class Measurement(_measurement_mapping.MeasurementMapping):
    """
    A Measurement is a container for :py:class:`.Sub` objects.
    Measurements can have any number of Subs within a single measurement,
    and each Sub can have any number of numeric values within that sub.

    Measurements can be loaded from a file using the 
    :func:`.load` function.  

    Constructing a new measurement can be done in two ways:

        1.) Calling :py:class:`.Measurement` with a string name, or no argument
        2.) Calling :py:meth:`.Measurement.new`

    In
