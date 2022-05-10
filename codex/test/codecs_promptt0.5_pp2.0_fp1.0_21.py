import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

