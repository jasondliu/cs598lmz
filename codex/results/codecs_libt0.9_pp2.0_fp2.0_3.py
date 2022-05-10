import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

command1="g++ "+sys.argv[1]

arguments=sys.argv[2:]
process  = subprocess.Popen([command1]+arguments,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,Shell=False)

while True:
    output=process.stdout.readline()
    output=output.decode()
    if output == '' and process.poll() is not None:
        break
    if output:
        sys.stdout.write(output.strip())

command2=".\\a.exe"
process = subprocess.Popen([command2],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

for line in process.stdout:
    print(line)
