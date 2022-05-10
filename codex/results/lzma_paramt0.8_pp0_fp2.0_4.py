from lzma import LZMADecompressor
LZMADecompressor().decompress(encoded)

# Decoding to Unicode
import sys
sys.getdefaultencoding()

# Built-in Error Classes
err = ValueError('invalid value')
err = ValueError('invalid value', 2)
err.args

err.with_traceback(tb)

def faulty():
    raise Exception('Something went wrong')

def ignore_exception():
    faulty()

def handle_exception():
    try:
        faulty()
    except:
        print('Exception handled')

handle_exception()
ignore_exception()

def describe_city(city, country='norway'):
    print(f'{city.title()} is in {country.title()}.')

describe_city('santiago')
describe_city('reykjavik', 'iceland')

def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first
