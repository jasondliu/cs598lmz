import weakref
import xml.etree.cElementTree  as ET



def setXSDataInputRaddosev10(xsDataInputRaddosev10, _edPlugin=None):
    """
    This method takes a XSDataInputRaddosev10 object and a EDPluginControl instance
    as arguments, and creates an instance of the Raddose v1.0 control plugin
    class.
    """
    edPluginControlRaddosev10 = EDPluginControlRaddosev10(_edPlugin)
    edPluginControlRaddosev10.setBaseDirectory(_edPlugin.getWorkingDirectory())
    xsDataInputRaddosev10.crystal.weight.value = float(xsDataInputRaddosev10.getCrystal().getWeight().getValue())
    xsDataInputRaddosev10.crystal.density.value = float(xsDataInputRaddosev10.getCrystal().getDensity().getValue())
    xsDataInputRaddosev10.photonenergy.value = float(xsDataInputRaddosev10.photonenergy.value)

