import bz2
bz2File = bz2.BZ2File('/tmp/da.bz2')
data = bz2File.read()
bz2File.close()

print(data)

# Exporting data networks
from_addr = 'projects@codebytes.in'
to_addr = 'some_user@some_host.some_tld'
import smtplib
ser = smtplib.SMTP()
try:
	ser.connect('localhost', '8025')
	ser.sendmail(from_addr, to_addr, data)
except:
	pass
finally:
	ser.quit()
