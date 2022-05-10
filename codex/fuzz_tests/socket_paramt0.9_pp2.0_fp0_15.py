import socket
socket.if_indextoname('12')

# 根据一个局域网网卡获取全部网卡
import psutil,netifaces
netifaces.interfaces()

# 根据网卡查看IP
netifaces.ifaddresses('en1')
netifaces.ifaddresses('en1')[netifaces.AF_INET]


# Xcode 技巧记录
# 打开开发者官网
https://developer.apple.com/

# 第三方知识点
# 打包 iOS 应用的第三方应用
fastlane （http://fastlane.tools/)


```

```
对象相关
# 只看对象的内部成员
po 0x10010a100.__
