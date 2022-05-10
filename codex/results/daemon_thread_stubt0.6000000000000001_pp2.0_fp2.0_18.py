import sys, threading

def run():
	os.system("scrapy crawl baiduSpider")

threads = []
t1 = threading.Thread(target=run)
threads.append(t1)
t2 = threading.Thread(target=run)
threads.append(t2)
t3 = threading.Thread(target=run)
threads.append(t3)

if __name__ == '__main__':
	for t in threads:
		t.setDaemon(True)
		t.start()
	t.join()
	print("all over %s" %ctime())
