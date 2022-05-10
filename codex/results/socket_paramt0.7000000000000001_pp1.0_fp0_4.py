import socket
socket.if_indextoname(socket.if_nametoindex('eth0'))

# ftp模块
import ftplib
ftp = ftplib.FTP('ftp.debian.org')
ftp.login()
ftp.cwd('debian')
ftp.quit()

# telnet模块
import telnetlib
tel = telnetlib.Telnet('192.168.0.2')
tel.write('girish\n')
tel.write('password\n')
tel.write('ls\n')
tel.write('exit\n')
print tel.read_all()

# smtplib模块
import smtplib
server = smtplib.SMTP('192.168.0.2')
server.sendmail('girish@redhat.com', 'girish@redhat.com', 'this is a test')
server.quit()

# poplib模块
import poplib
server = poplib.POP3('192.168.0.2')

