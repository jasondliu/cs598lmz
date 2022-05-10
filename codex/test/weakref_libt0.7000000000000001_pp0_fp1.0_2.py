import weakref

import hdtv.config
import hdtv.cmdline
import hdtv.options

# Object to store fit information
class Fit(object):
    def __new__(cls, fitID, energy, value, error, fit_energy, fit_value, fit_error):
        # Check if fitID is a valid identifier
        if not is_identifier(fitID):
            raise ValueError("%s is not a valid identifier" % fitID)
        # Check if energy is a float
        if type(energy) != float:
            raise ValueError("Energy is not a float")
        # Check if value is a float
        if type(value) != float:
            raise ValueError("Value is not a float")
        # Check if error is a float
        if type(error) != float:
            raise ValueError("Error is not a float")
        # Check if fit_energy is a float
        if type(fit_energy) != float:
            raise ValueError("Fit_energy is not a float")
        # Check if fit_value is a float
