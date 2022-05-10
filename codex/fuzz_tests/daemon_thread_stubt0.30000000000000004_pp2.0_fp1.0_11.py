import sys, threading

def run():
	os.system('python3 -m pip install -r requirements.txt')
	os.system('python3 main.py')

def main():
	if len(sys.argv) < 2:
		print('Usage: python3 run.py [install]')
		sys.exit()

	if sys.argv[1] == 'install':
		threading.Thread(target=run).start()
		print('Installing requirements...')
		print('This may take a while...')
		print('Please wait...')
		print('[*] Done!')
		print('[*] Starting main.py...')
		print('[*] Done!')
	else:
		print('Usage: python3 run.py [install]')
		sys.exit()

if __name__ == '__main__':
	main()
