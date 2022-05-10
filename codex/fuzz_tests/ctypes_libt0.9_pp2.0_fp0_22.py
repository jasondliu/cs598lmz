import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

def load_file(the_file):
  return open(the_file, "r", encoding='utf-8').read()

def parse(data):
  print('parse called')
  return [i.strip() for i in data.split('\n') if i]

data = load_file('test.txt')

executable_list = parse(data)

def main():
  print('main called')

  for executable in executable_list:
    print(executable)

main()
</code>
Why can't I see my windows files with this code?
Who is "administrator" and how do I get their files?


A:

You are specifying the path with the file name. You need to change that to <code>C:\Windows</code>
<code>data = load_file('C:\Windows')
</code>
I hope this helps. (Also, you can use <code>os.listdir(location)</code> to list the files)

