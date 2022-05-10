import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls() 
# Authentication 
s.login("prashantrastogi2022@gmail.com", "Practo@123") 
# message to be sent 
print("hii")
message = 'hello ji ho gya'
print("hi3")
# sending the mail 
s.sendmail("senders_email_id", "receivers_email_id", message) 
# terminating the session 
s.quit()

#python graphics.py 'another message'
