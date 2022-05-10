fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

try:
    fn()
except TypeError as err:
    print("TypeError:", err)

# accessing __code__ attribute is warning in 3.7
import warnings
warnings.simplefilter("ignore", PendingDeprecationWarning)

fn.__code__ = gi
fn()
