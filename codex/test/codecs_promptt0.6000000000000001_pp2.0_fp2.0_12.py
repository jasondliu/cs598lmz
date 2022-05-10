import codecs
# Test codecs.register_error('strict', strict_errors)
# Test codecs.register_error('ignore', ignore_errors)
# Test codecs.register_error('replace', replace_errors)

import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
