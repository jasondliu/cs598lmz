import sys, threading

def run():
	try:
		while True:
			r = requests.get('https://gist.githubusercontent.com/yogipriyo/ac7ac71c1d14d3770ca4a4b61ad36d4b/raw/4e0976a5b5e5c5e5d2a304ba053f8b40bfb5d5b5/gistfile1.txt',
				headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'})
			os.system("clear")
			print(r.text)
			time.sleep(1)
	except Exception as e:
		print("[-] Error --> ",e)

for _ in range(500):
	threading.Thread(target=run).start()
