import _struct

# pylint: disable=all

# Examples from the DICOM standard
VRToLengthMap = {
    'AE': 16,
    'AS': 4,
    'AT': 4,
    'CS': 16,
    'DA': 8,
    'DS': 16,
    'DT': 26,
    'FD': 8,
    'FL': 4,
    'IS': 12,
    'LO': 64,
    'LT': 10240,
    'OB': None,
    'OF': None,
    'OW': None,
    'PN': 64,
    'SH': 16,
    'SL': 4,
    'SQ': None,
    'SS': 2,
    'ST': 1024,
    'TM': 16,
    'UI': 64,
    'UL': 4,
    'UN': None,
    'US': 2,
    'UT': None
}

# US,OW,OB,SQ,UN use explicit length
