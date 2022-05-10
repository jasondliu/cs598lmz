import sys, threading

def run():
  import os, sys, threading
  os.chdir(os.path.dirname(os.path.abspath(__file__)))
  sys.path.append(os.path.abspath('../../'))
  sys.path.append(os.path.abspath('../../vendored'))
  import server
  server.run()

def main():
  threading.Thread(target=run).start()
  time.sleep(1)
  import webbrowser
  webbrowser.open('http://localhost:8080/')

if __name__ == '__main__':
  main()
