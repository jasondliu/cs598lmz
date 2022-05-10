import mmap
import os
import re
import smtplib
import sys
import time

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formatdate

# 发送邮件
def send_mail(mail_from, mail_to, subject, content):
    msg = MIMEMultipart()
    msg['From'] = mail_from
    msg['To'] = mail_to
    msg['Subject'] = Header(subject, 'utf-8')
    msg['Date'] = formatdate()
    msg.attach(MIMEText(content, 'plain', 'utf-8'))

    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login('cq_sender@163.com', 'Cq_sender')
        smtp.sendmail(mail_from, mail_to, msg.as_string())
        smtp
