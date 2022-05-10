import sys, threading

def run():
    global thread_list
    while True:
        try:
            url = url_list.pop()
        except:
            break
        try:
            print url
            r = requests.get(url, timeout=10)
            data = r.text
            # print data
            # exit(1)
            p = re.compile(r'<a href="(.*?)" class="s xst"', re.S)
            title_list = p.findall(data)
            for item in title_list:
                print item
                title_file.write(item + "\n")
        except:
            pass
    print "thread exit"

if __name__ == "__main__":
    title_file = open("title.txt", "w")
    url_list = []
    for i in xrange(1, 230):
        url_list.append("http://bbs.tianya.cn/list-free-1-" + str(i) + ".shtml")
    thread_list = []
    for i in range(20):
        t
