import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
# these are descriptions of the UMLS automatically mismapped by the
# following script.
#
# note that this list is not exhaustive (anything I didn't catch,
# please send it to me.)
#
# "code" : (string, type, cui),
#
MISMATCH = {
#    "BACTERIAL IDENTIFICATION" : ("bacterial", None, "C3665961"),
    "BITTERNESS" : ("taste_bitter", "Substance", "C0010200"),
    "CHOKING" : ("choking", "Biomedical_or_Dental_Malfunction", "C1510906"),
#    "EARLIER STAGE" : ("earlier_stage", None, None),
#    "ENDOSCOPIC ULTRASOUND FNA" : ("endoscopic_ultrasound", None, None),
#    "FACILITY INFO" : ("facility_info", None, None),
#    "HISTORY OF SURGERY" : ("history_of_
