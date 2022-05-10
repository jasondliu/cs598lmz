gi = (i for i in ())
# Test gi.gi_code.co_code


def getiters():
    return iter([1, 2, 3])


it = getiters()
# Test it.gi_frame.f_code.co_code
it = (i for i in [1, 2, 3])
# Test it.gi_code.co_code


def getdictviews():
    return {1: "1"}.items()


dv = getdictviews()
# Test dv.dv_code.co_code or dv.dv_code.co_filename


def getdictviewkeys():
    return {1: "1"}.keys()


dv = getdictviewkeys()
# Test dv.dv_code.co_code or dv.dv_code.co_filename


def getdictviewvalues():
    return {1: "1"}.values()


dv = getdictviewvalues()
# Test dv.dv_code.co_code or dv.dv_code.co_filename


def getdictiter():
    return {1: "1"}
