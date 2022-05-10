import bz2
bz2.BZ2File(filename)

import gzip
gzip.open(filename)

import lzma
lzma.LZMAFile(filename)

import zipfile
z = zipfile.ZipFile(filename)
z.namelist()
z.getinfo('file.txt')
z.read('file.txt')

from urllib.request import urlopen
for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    line = line.decode('utf-8')
    if 'EST' in line or 'EDT' in line:
        print(line)

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
                """To: jcaesar@example.org
                From: soothsayer@example.org

                Beware the Ides of March.
                """)
server.quit()

from datetime import date
now = date.today()
now
