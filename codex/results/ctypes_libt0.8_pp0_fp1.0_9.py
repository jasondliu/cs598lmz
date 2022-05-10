import ctypes
ctypes.windll.user32.MessageBoxW(0, "自動化餵食成功", "***恭喜***", 1)

#清除網頁上的資料
browser.delete_all_cookies()
browser.close()

time.sleep(5)

#送出簡訊
url = 'https://api.twilio.com/2010-04-01/Accounts/AC98e743927ff0d4a4f4374117a86f08c7/Messages.json'
data = {
    'To':      '+886932158411',
    'From':    '+12055700829',
    'Body':    '已經餵食完畢',
}

twilio_auth = ('AC98e743927ff0d4a4f4374117a86f08c7', '3e44f89c607d1c22ecff028
