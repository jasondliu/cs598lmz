import socket
socket.if_indextoname(2)

# 全てのIPアドレスを取得する
socket.gethostbyname_ex('hostname')

# アドレス変換
socket.gethostbyaddr('127.0.0.1')

# サーバを探す
socket.gethostbyname('hostname')

# サーバのアドレスを取得する
socket.gethostname()

# ユーザ名取得
socket.getfqdn('127.0.0.1')

# 実行ユーザのホームディレクトリを取得する
socket.gethostbyname(socket.gethostname())


import smtplib
# SMTPサーバを指定
smtp = smtplib.SMTP('smtp.mail.yahoo.co.jp',587)
smtp.ehlo()

# SMTPの認証
