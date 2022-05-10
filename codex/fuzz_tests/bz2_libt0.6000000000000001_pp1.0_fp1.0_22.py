import bz2
bz2.decompress(bz2.compress(b'hello world'))

# Example: Using JSON
import json
json.dumps([1, 'simple', 'list'])

# Example: Using XML
from xmlrpc.client import ServerProxy
s = ServerProxy('http://localhost:9000')
s.get_multiply(10, 20)

# Example: Using Emails
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
server.quit()

# Example: Using Dates and Times
from datetime import date
now = date.today()
now
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

# Example: Manipulating Strings
birthday = date(1964, 7, 31)
age
