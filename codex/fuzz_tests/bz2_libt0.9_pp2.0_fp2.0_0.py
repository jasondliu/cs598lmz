import bz2
bz2.compress(data)

# md5 计算摘要
# md5可以用来检查文件的完整性
import hashlib
hashlib.md5(data).hexdigest()

# 邮件库 smtplib imaplib email
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

# 发送邮件
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# msg = MIMEText('hello world')
msg = MIMEText('<html><body><h1>Hello</h1>' +
        '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
        '</body></html>', 'html
