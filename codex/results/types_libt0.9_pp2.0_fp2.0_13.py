import types
types.ClassType
#<type 'classobj'>
types.StringType
#<type 'string'>
types.UnicodeType


# Input
# get user input, defaults to strings
user_input = raw_input('Enter a number: ')
# "01"
user_input = raw_input('Enter a number: ')
# "E"

# int() will attempt to parse user input, however it wil blow up if anything other than a number is typed in
result = int(user_input) + 2
# ValueError: invalid literal for int() with base 10: 'E'

# fstring
# format strings using he python's native string formatting
name = 'RV'
weight_lbs = 150
# The quick brown {name} jumps over the lazy {weight_lbs}-pound dog.
# 'The quick brown RV jumps over the lazy 150-pound dog.'

# output
# data can be sent to standard output using the print statement
x = "my value is"
print x + " foo"
# my value is foo

print "my value is", x
# my value is my
