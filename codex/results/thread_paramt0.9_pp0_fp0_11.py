import sys, threading
threading.Thread(target=lambda:sys.stdout.write(s[6:]+'\n')).start()
sunrin.init()
# 인증서를 통해 컴퓨터, 코드에 대한 권한을 인식

# 선린인터넷고등학교

wifi_username = input('SunrinWiFi ID:')
# 위의 사항을 통해 인증할 사용자 아이디 
wifi_password = input('SunrinWiFi PW:')
# 위에 아이디를 통해 인증할 암호
my_code = input('Your Code:')
# 코드를 통해
