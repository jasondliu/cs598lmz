import select
# Test select.select
# 打开文件, 把文件句柄注册到监听的列表中
rlist = [open("/etc/services")]
wlist = []
xlist = []
while True:
    # select.select(rlist,wlist,xlist)接受三个列表,[],[],[]
    print("开始监控")
    result_rlist,result_wlist,result_xlist = select.select(rlist,wlist,xlist)
    print("结束监控")
    
    for r in result_rlist:
        data = r.read()
        print(data)
        if not data:
            rlist.remove(r)  
            
    for w in result_wlist:
        pass
    for x in result_xlist:
        pass
