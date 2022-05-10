gi = (i for i in ())
# Test gi.gi_code
# TypeError: Required argument 'n' (pos 1) not found
# gi.gi_code = 0
# Test AttributeError on delete
try :
    del gi.gi_code
except AttributeError:
    pass
else :
    raise Exception, 'expected AttributeError'
# Test AttributeError on delelete
try :
    del gi.gi_running
except AttributeError:
    pass
else :
    raise Exception, 'expected AttributeError'
