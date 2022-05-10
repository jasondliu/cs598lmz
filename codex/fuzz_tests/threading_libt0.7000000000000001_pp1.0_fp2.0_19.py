import threading
threading.stack_size(67108864)

u = up()

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 {} <version>'.format(sys.argv[0]))
        print('Example: python3 {} 1.3'.format(sys.argv[0]))
        sys.exit(1)

    u.user_id = os.environ.get('SLACK_USER_ID')
    u.token = os.environ.get('SLACK_TOKEN')
    u.api_call('chat.postMessage', channel=u.user_id, text='Starting upload to PyPI of pyslackers version {}'.format(sys.argv[1]))

    try:
        u.upload(sys.argv[1])
    except Exception as e:
        u.api_call('chat.postMessage', channel=u.user_id, text='Failed uploading pyslackers version {}'.format(sys.argv[1]))
        raise e
    else:
        u.api
