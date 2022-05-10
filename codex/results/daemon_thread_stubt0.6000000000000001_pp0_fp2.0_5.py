import sys, threading

def run():
  os.chdir('/Users/charlie/Desktop/python/')
  os.system('python3 main.py')

def main():
  t = threading.Thread(target=run)
  t.start()
  time.sleep(5)
  os.system('pkill -f "python3 main.py"')
  os.system('open https://www.google.com')
  print('done')

main()
</code>

