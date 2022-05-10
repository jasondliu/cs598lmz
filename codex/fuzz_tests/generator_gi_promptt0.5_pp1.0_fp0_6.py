gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print('AttributeError expected')
# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    print('AttributeError expected')
# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    pass
else:
    print('AttributeError expected')
# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test Illegal instruction
try:
    raise ValueError('test')
except ValueError as e:
    try:
        e.__traceback__.tb_next
    except AttributeError:
        pass
    else:
        print('AttributeError expected')
    try:
        e.__traceback__.tb_frame
    except AttributeError:
        pass
    else:
        print('AttributeError
