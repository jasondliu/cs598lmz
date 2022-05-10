import codecs
codecs.register_error('subjectServerQuot', subjectServerQuot)
codecs.register_error('subjectQuot', subjectQuot)

########################################################################
# クライアントから送られてくるメールをサーバー上で処理する
########################################################################
class mailServer(LineReceiver):
    "メールサーバー"
    #----------------------------------------------------------------------
    # 初期化
    #----------------------------------------------------------------------
    def __init__(self,users,domains):
        "初期化"
        self.state = "waitForMAIL" # メール受信状態:バナー待ち=1, EHLO待ち=2, 送信元待ち=3, RCPT待ち=4, データ送信待ち=5, データ送信中=6
        self.serverName = "mailServer1.babidore.org" # サーバー名
       
