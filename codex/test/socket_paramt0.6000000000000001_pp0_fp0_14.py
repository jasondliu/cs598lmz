import socket
socket.if_indextoname(3)

import re
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

# Function for checking password
def check(password):
    if (len(password)<8):
        return 'Password must be at least 8 characters'
    elif (len(password)>20):
        return 'Password must be at most 20 characters'
    elif not re.search('[a-z]', password):
        return 'Password must contain at least one lowercase character'
    elif not re.search('[A-Z]', password):
        return 'Password must contain at least one uppercase character'
    elif not re.search('[0-9]', password):
        return 'Password must contain at least one digit'
    elif not re.search('[@_!#$%^&*()<>?/\|}{~:]', password):
        return 'Password must contain at least one special character'
    else:
        return 'Valid Password'


# Main program
