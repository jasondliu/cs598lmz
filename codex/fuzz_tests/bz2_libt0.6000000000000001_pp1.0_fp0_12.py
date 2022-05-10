import bz2
bz2.open('examples/test.bz2')

# open a gzip compressed file
import gzip
gzip.open('examples/test.gz')

# import a module from a package
import twilio.rest

# import a module from a package and give it a short name
import twilio.rest as tr

# import a specific function from a package
from twilio.rest import get

# import a specific function from a package and give it a short name
from twilio.rest import get as tw_get

# import multiple functions at once
from twilio.rest import get, post

# import multiple functions at once and give them short names
from twilio.rest import get as tw_get, post as tw_post

# import all functions in a package
from twilio.rest import *

# import all functions in a package and give them short names
from twilio.rest import * as tw

# import a nested module
from twilio.rest import resources

# import a nested module and give it a short name
from twilio.
