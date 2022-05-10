import codecs
# Test codecs.register_error
# example file courtesy of Steve D'Aprano

# The file test.txt is encoded in iso-8859-1.
# It contains the following lines:
#
# âNow is the time for all good men to come to the aid of the party.â
# âNow is the time for all good men to come to the aid of the party.â
# âNow is the time for all good men to come to the aid of the party.â
# âNow is the time for all good men to come to the aid of the party.â
# âNow is the time for all good men to come to the aid of the party.â
# âNow is the time for all good men to come to the aid of the party.â

# for Python 2.4, add a register_error function
def register_error(errors, name):
    def handler(exc):
        if is
