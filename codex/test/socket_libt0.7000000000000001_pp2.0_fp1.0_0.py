import socket

def send_email(id_, name_, status, product_id, email_id, server = "smtp.gmail.com", port = 587,
              username = "", password = "", use_tls = True):
    FROM = username
    TO = [email_id]
    SUBJECT = "Order Status"
    TEXT = "Your order " + id_ + " for " + name_ + " is " + status
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP(server, port)
        if use_tls:
            server.starttls()
        server.login(username, password)
        server.sendmail(FROM, TO, message)
        server.quit()
    except smtplib.SMTPException as e:
        print(e)

