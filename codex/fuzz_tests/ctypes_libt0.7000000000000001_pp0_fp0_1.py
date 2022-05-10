import ctypes
ctypes.windll.user32.LockWorkStation()

print("computer locked")

#send email to my phone
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("karthik.prince26@gmail.com", "emailpassword")
server.sendmail(
  "karthik.prince26@gmail.com", 
  "7342496507@vtext.com", 
  "Computer has been locked")
server.quit()

print("email sent")
