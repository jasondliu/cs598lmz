gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print('AttributeError expected')

# __getattribute__ -> AttributeError
try:
    gi.gi_code = 1
except AttributeError:
    pass
else:
    print('AttributeError expected')

# __setattr__ -> AttributeError
try:
    gi.gi_code += 1
except AttributeError:
    pass
else:
    print('AttributeError expected')

# __getattribute__ -> TypeError
try:
    gi.gi_code += 1
except TypeError:
    print('TypeError: ' + str(gi))
else:
    print('TypeError expected')

# __setattr__ -> TypeError
try:
    gi.gi_code += 1
except TypeError:
    print('TypeError: ' + str(gi))
else:
    print('TypeError expected')
