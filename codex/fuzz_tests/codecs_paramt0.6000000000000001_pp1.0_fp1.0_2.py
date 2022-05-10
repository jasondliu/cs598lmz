import codecs
codecs.register_error('strict', codecs.ignore_errors)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def make_file_name(topic, n):
    return f'topics/{topic}/{topic}_{n}.txt'

def get_file_list(topic):
    return glob.glob(f'topics/{topic}/{topic}_*.txt')

def make_topics(topic, n):
    if os.path.exists(f'topics/{topic}'):
        eprint(f'{topic} directory exists. Please delete it first.')
        return
    os.makedirs(f'topics/{topic}')
    print(f'Created {topic} directory')

    payload = {'topic': topic, 'n': n, 'lang': 'en'}
    r = requests.get('http://www.gutenberg.org/ebooks/search/', params=payload)
    soup = BeautifulSoup(r.text, 'html
