import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Searching for devices...\n')).start()

adb_cmd =  'adb devices'
p = subprocess.Popen(adb_cmd, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output, err = p.communicate()
lines = err
if lines == '':
	lines = output
lines = lines.split('\n')
devices = []
for line in lines:
	if 'device' in line and 'devices' not in line:
		dev = line.split('\t')[0]
		if dev not in devices:
			devices.append(dev)

if len(devices) == 0:
	os.system('cls')
	sys.stdout.write('Restart adb and connect device,')
	sys.stdout.write('Check Device Manager for correct driver installation (Google ADB composite)\n')
