import ctypes
ctypes.windll.user32.LockWorkStation()  # ロック

# ↓検索中です・・・（このロックfor解除スクリプト(Windowsロック用解除スクリプト）は不要でした。）

# 待機時間？
# if int(now.minute)==10 :
#    pyautogui.PAUSE = 60
# else:
#    pyautogui.PAUSE = 1
#    # print (now.minute)


# 以下やること
# ・対象画像の「x座標,y座標」を求める。
# ・対象アプリの「x座標,y座標」を求める。
# ・対象画像(座標)を
