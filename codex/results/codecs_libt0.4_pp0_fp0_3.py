import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

#----------------------------------------------------
# クラス定義
#----------------------------------------------------
# ログ出力用クラス
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout  # 保存
        self.log = open("log.txt", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

#----------------------------------------------------
# 関数定義
#----------------------------------------------------
# 引数の値を数値に変換する
def convert_to_int(value):
    if value == '':
        return 0
    else:
        return int(value)

#----------------------------------------------------
# メイン処理
#----------------------------------------------------
if __name__ == '__main__':
    # ログ出
