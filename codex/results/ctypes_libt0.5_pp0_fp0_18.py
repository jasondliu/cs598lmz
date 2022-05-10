import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#Downloading files from the web
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

#Sending emails
import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn)
conn.ehlo()
conn.starttls()
conn.login('email', 'password')
conn.sendmail('from', 'to', 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
conn.quit()

#Reading and writing files
helloFile = open('C:\\Users\\Al\\Documents\\hello.txt')
helloFile.read()
helloFile.close()

#Reading and
