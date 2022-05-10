import sys, threading

def run():
    os.system('python ' + config['app']['filename'])

os.system('clear')

print('CHECKING CONFIG FILE')

with open('config.json', 'r') as f:
    config = json.loads(f.read())

if not os.path.isfile(config['app']['filename']):
    print('ERROR: FILE ' + config['app']['filename'] + ' NOT FOUND')
    sys.exit(1)

print('  OK ')

print()

print('CHECKING UPLOAD FOLDER')

if not os.path.exists(config['app']['upload_folder']):
    print('ERROR: ' + config['app']['upload_folder'] + ' NOT EXISTS')
    sys.exit(1)

if config['app']['upload_folder'][-1] != '/':
    print('ERROR: ' + config['app']['upload_folder'] + ' MUST END WITH "/"')
    sys.exit(1)

print('  OK ')

