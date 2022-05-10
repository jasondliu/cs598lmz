import select

def main():
    # 创建套接字作为监控IO
    rlist = []
    wlist = []
    xlist = []
    rs, ws, xs = select.select(rlist, wlist, xlist)
    print("监测IO:", rs, ws, xs)

if __name__ == "__main__":
    main()
