import signal
signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

'''
生日签到脚本 V0.1
将此脚本放到服务器上，可以实现定时签到
'''

# 主要参数如下
# 如果要获取用户昵称，就在chrome开发者界面中找到 xhr -> event 就可以看到
# 还是建议手动登陆之后手动获取token，因为那个会有很多额外的参数，token无需decode

# 
