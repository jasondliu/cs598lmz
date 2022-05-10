import socket
# Test socket.if_indextoname()
# 特定のインターフェースに接続されたインデックス番号を取得
print(socket.if_indextoname(1))

# Test socket.if_nameindex()
# 全てのインターフェースに接続されたインデックス番号と名前を辞書型で取得
print(socket.if_nameindex())

# Test socket.gethostname()
# ホスト名を取得
print(socket.gethostname())

# Test socket.gethostbyname()
# ホスト名からIPアドレスを取得
print(socket.gethostbyname("www.google.com"))

# Test socket.gethostbyname_ex()
# ホスト名からIPアドレス、アドレスタイプ、アドレスのリストを取得
