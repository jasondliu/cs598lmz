import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class SendMail():
    def __init__(self, to_list, sub, content):
        self.to_list = to_list
        self.sub = sub
        self.content = content
        self.mail_host = "smtp.qq.com"
        self.mail_user = "793886244@qq.com"
        self.mail_pass = "hkwwxgzxuzjtcjcc"
        self.mail_postfix = "qq.com"

    def send_mail(self):
        me = "hello" + "<" + self.mail_user + "@" + self.mail_postfix + ">"
        msg = MIMEText(self.content, _subtype='plain', _charset='utf-8')
        msg['Subject'] = self.sub
        msg['From'] = me
        msg['To'] = ";".join(self.to_list)
        try:
            server = sm
