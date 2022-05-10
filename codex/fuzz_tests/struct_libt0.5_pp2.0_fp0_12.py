import _struct

# *****************************************************************************
# ************************* Global variables **********************************
# *****************************************************************************

# *****************************************************************************
# ************************* Functions *****************************************
# *****************************************************************************
def get_version():
    """
    Get version of the library
    """
    return _struct.get_version()

def get_version_string():
    """
    Get version string of the library
    """
    return _struct.get_version_string()

def get_version_tuple():
    """
    Get version tuple of the library
    """
    return _struct.get_version_tuple()

def get_version_major():
    """
    Get major version number of the library
    """
    return _struct.get_version_major()

def get_version_minor():
    """
    Get minor version number of the library
    """
    return _struct.get_version_minor()

def get_version_patch():
    """
    Get patch version number of the library
    """
    return _struct.get_version_
