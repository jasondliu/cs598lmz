gi = (i for i in ())
# Test gi.gi_code

try:
    x = gi.gi_code
except AttributeError:
    print('AttributeError')
except RuntimeError as e:
    print(e)

# Test gi.gi_frame

try:
    x = gi.gi_frame
except AttributeError:
    print('AttributeError')
except RuntimeError as e:
    print(e)

# Test gi.gi_running

try:
    x = gi.gi_running
except AttributeError:
    print('AttributeError')
except RuntimeError as e:
    print(e)

# Test gi.gi_yieldfrom

try:
    x = gi.gi_yieldfrom
except AttributeError:
    print('AttributeError')
except RuntimeError as e:
    print(e)

# Test gi.send()

try:
    x = gi.send(2)
except TypeError:
    print('TypeError')
except StopIteration:
    print('StopIteration')
except RuntimeError as e:
    print(
